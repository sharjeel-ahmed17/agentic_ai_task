import asyncio
from agents import Agent, Runner, SQLiteSession
from agentsdk_gemini_adapter import config

# Create agent
agent = Agent(
    name="Assistant",
    instructions="Reply very concisely.",
)
# Create a session instance with a session ID
session = SQLiteSession("conversation_123")
async def main():


    # First turn (async)
    result = await Runner.run(
        agent,
        "What city is the Golden Gate Bridge in?",
        session=session,
        run_config=config
    )
    print(result.final_output)  # "San Francisco"

    # Second turn (async)
    result = await Runner.run(
        agent,
        "What state is it in?",
        session=session,
        run_config=config
    )
    print(result.final_output)  # "California"

# Synchronous call (no await needed)
# result = Runner.run_sync(
#     agent,
#     "What's the population?",
#     session=session,
#     run_config=config
# )
# print(result.final_output)  # "Approximately 39 million"

# Run the async function
asyncio.run(main())
