import asyncio
from agents import Agent, Runner
from agentsdk_gemini_adapter import config
async def main():
    agent: Agent = Agent(name="Assistant", instructions="ou only respond in haikus.")
    result = await Runner.run(agent,"Tell me about recursion in programming.",run_config=config)
    print(result.final_output)
if __name__ == "__main__":
    asyncio.run(main())