#!/bin/bash

# Miner-X: Autonomous B2B Prospecting Engine (V3.0) 
# Setup and Install Script

set -e # Stop on error

echo "🚀 [Miner-X] Initializing setup environment..."

# 1. System Update and Dependency Installation
echo "📦 Updating system packages..."
sudo apt-get update && sudo apt-get install -y \
    python3-pip \
    python3-venv \
    git \
    curl \
    docker.io \
    docker-compose

# 2. Start Docker Service
echo "🐳 Configuring Docker..."
sudo systemctl start docker
sudo systemctl enable docker

# 3. Create Project Directory Structure
echo "📂 Initializing project folders..."
mkdir -p core tools data logs

# 4. Initialize Python Virtual Environment
echo "🐍 Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip

# 5. Generate requirements.txt
cat <<EOF > requirements.txt
crewai
litellm
langchain_openai
requests
holehe
email-validator
asyncio
python-dotenv
crawl4ai
pandas
openpyxl
tqdm
EOF

# 6. Install Python Dependencies
echo "pip installing core dependencies (this may take a few minutes)..."
pip install -r requirements.txt

# 7. Initialize .env file from example if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Generating .env config from example..."
    cp .env.example .env
    echo "✅ .env file created. Please edit it with your API keys and GUID."
else
    echo "⚠️ .env already exists. Skipping overwrite."
fi

# 8. Start Docker Services
echo "🚀 Starting Docker services (Scraper & SpiderFoot)..."
docker-compose up -d

echo "------------------------------------------------"
echo "🎉 [Miner-X] Installation Complete!"
echo "------------------------------------------------"
echo "Next Steps:"
echo "1. Run 'source venv/bin/activate' to enter virtual environment."
echo "2. Run 'nano .env' to add your LLM API Key and ABN GUID."
echo "3. Run 'python core/engine.py' to start your first B2B Prospecting Session."
echo "------------------------------------------------"
