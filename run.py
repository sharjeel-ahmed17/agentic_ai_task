from agents import Agent, Runner
from agentsdk_gemini_adapter import config
agent: Agent = Agent(name="Assistant", instructions="You are a helpful assistant")
result = Runner.run_sync(agent, "Hello, how are you.", run_config=config)
print(result.final_output)