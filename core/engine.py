import asyncio
import os
from typing import List, Dict, Any
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from core.llm_wrapper import LLMAdapter
from tools.au_abn_lookup import ABNValidator
from tools.social_verify import verify_social_presence
from tools.smtp_verifier import SMTPVerifier

class MinerXEngine:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        # LiteLLM Unified Wrapper
        self.llm = ChatOpenAI(
            model=config.get("model", "deepseek/deepseek-chat"),
            api_key=os.getenv("LLM_API_KEY"),
            base_url=os.getenv("LLM_BASE_URL")
        )
        self.abn_validator = ABNValidator(os.getenv("ABN_GUID"))
        self.smtp_verifier = SMTPVerifier()

    def _create_agents(self) -> List[Agent]:
        """Create specialized Agents for B2B Mining"""
        
        # 1. Market Researcher
        researcher = Agent(
            role='Market Researcher',
            goal='Extract core business focus and recent news for {company}',
            backstory='Expert in analyzing Australian B2B company websites and news signals.',
            llm=self.llm,
            verbose=True
        )

        # 2. Identity Lock Specialist
        identity_lock = Agent(
            role='Identity Specialist',
            goal='Identify the Founder or CEO name and LinkedIn profile for {company}',
            backstory='Master of OSINT, skilled at finding decision makers from "About Us" or PR pages.',
            llm=self.llm,
            verbose=True
        )

        # 3. Outreach Strategist
        strategist = Agent(
            role='Sales Strategist',
            goal='Create a high-converting ice-breaker based on the founder background',
            backstory='Expert in personalized B2B outreach with 15 years experience in Supply Chain sales.',
            llm=self.llm,
            verbose=True
        )

        return [researcher, identity_lock, strategist]

    async def process_single_lead(self, lead_data: Dict[str, Any]) -> Dict[str, Any]:
        """Main pipeline for a single lead"""
        company_name = lead_data.get("name")
        abn = lead_data.get("abn")

        print(f"🚀 [Miner-X] Processing Lead: {company_name}")

        # --- Step 1: Official ABN Check (Fast Fail) ---
        if abn:
            abn_result = self.abn_validator.validate(abn)
            if abn_result.get("status") != "Active":
                return {"status": "skipped", "reason": f"ABN Inactive or Not Found: {abn_result.get('status')}"}

        # --- Step 2: Multi-Agent Deep Dive ---
        agents = self._create_agents()
        tasks = [
            Task(description=f"Analyze {company_name} core business products and services.", agent=agents[0]),
            Task(description=f"Find the Founder/CEO name of {company_name} and their LinkedIn URL.", agent=agents[1]),
            Task(description=f"Draft a personalized B2B ice-breaker for {company_name}.", agent=agents[2])
        ]
        
        crew = Crew(agents=agents, tasks=tasks, process=Process.sequential)
        research_result = await asyncio.to_thread(crew.start)

        # --- Step 3: Social & SMTP Verification ---
        # Note: In a real run, the Identity Agent would output the email pattern
        # This is a placeholder for the logic flow
        potential_email = f"first.last@{company_name.lower().replace(' ', '')}.com.au" 
        
        is_smtp_valid = self.smtp_verifier.verify(potential_email)
        has_social = await verify_social_presence(potential_email)

        # --- Step 4: Confidence Scoring ---
        score = 0
        if is_smtp_valid: score += 40
        if has_social: score += 40
        if abn: score += 20

        return {
            "company": company_name,
            "research": str(research_result),
            "verified_email": potential_email if is_smtp_valid else "Needs Verification",
            "social_proof": has_social,
            "confidence_score": score,
            "status": "completed"
        }

    async def run_batch(self, leads: List[Dict[str, Any]]):
        """Batch processing with concurrency control"""
        semaphore = asyncio.Semaphore(10) 
        
        async def sem_task(lead):
            async with semaphore:
                return await self.process_single_lead(lead)

        tasks = [sem_task(l) for l in leads]
        return await asyncio.gather(*tasks)

if __name__ == "__main__":
    # Test runner
    import dotenv
    dotenv.load_dotenv()
    engine = MinerXEngine({"model": os.getenv("MODEL_NAME", "deepseek-chat")})
    asyncio.run(engine.run_batch([{"name": "Phipony Supply Chain", "abn": "11000000000"}]))
