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
    controller = Controller(output_model=Posts)
    agent1 = Agent(
            task=f'You will first be on the apollo website. On the right side of the page, there are a list of people in the industry with their information. We are looking for {num_people or NUM_PEOPLE} people who we can reach out to for a job or internship, so read their titles and find the most relevant people which I could reach out to. Click the access email button which reveals their email address. Get their name, title, company, and email address.',
            llm=ChatOpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"), temperature=0.00),
            browser=create_browser(),
            controller=controller
    )
    result = await agent1.run()

if __name__ == "__main__":
    asyncio.run(main())
