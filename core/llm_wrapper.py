import os
from typing import List, Dict, Any
import litellm

class LLMAdapter:
    """
    Unified LLM Adapter using LiteLLM to support any OpenAI-compatible API.
    Supports: Claude, GPT, DeepSeek, Ollama, etc.
    """
    def __init__(self, model_name: str = None):
        self.model = model_name or os.getenv("MINER_LLM_MODEL", "gpt-4o")
        self.api_key = os.getenv("MINER_LLM_API_KEY")
        
    def call(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """
        Generic call method for any model provider.
        """
        try:
            response = litellm.completion(
                model=self.model,
                messages=messages,
                api_key=self.api_key,
                **kwargs
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error calling LLM: {str(e)}"

# Example Usage:
# adapter = LLMAdapter(model_name="deepseek/deepseek-chat")
# response = adapter.call([{"role": "user", "content": "Extract CEO name from this text..."}])
