from browser_use import Agent, Browser, BrowserConfig, Controller
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import asyncio

# Get the current directory and construct the path to .env
current_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(current_dir, '.env')

print(f"Looking for .env file at: {env_path}")
# Load .env with override=True to ensure it takes precedence
load_dotenv(env_path, override=True)
api_key = os.getenv("OPENAI_API_KEY")
print(f"API Key loaded: {api_key}")

CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

# ========== BROWSER FUNCTIONS ==========
async def create_browser():
    """Create and return a new browser instance"""
    return Browser(
        config=BrowserConfig(
            chrome_instance_path=CHROME_PATH,
        )
    )

async def main():
    browser = await create_browser()
    agent1 = Agent(
        task=f'Go to linkedin.com and search for manual labor jobs in Texas and apply to one of them',
        browser=browser,
        llm=ChatOpenAI(model="gpt-4o", api_key=api_key)
    )
    result = await agent1.run()

if __name__ == "__main__":
    asyncio.run(main())
