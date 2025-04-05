from browser_use import Agent, Browser, BrowserConfig, Controller
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

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
    agent1 = Agent(
        task=f'Go to linkedin.com and search for manual labor jobs in Texas and apply to one of them',
        browser=create_browser(),
        llm=ChatOpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))
    )
    result = await agent1.run()

if __name__ == "__main__":
    asyncio.run(main())
