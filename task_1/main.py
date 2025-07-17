from agents import Agent , Runner
from agentsdk_gemini_adapter import config
agent = Agent(
    name="Math Tutor",
    instructions="You provide help with math problems. Explain your reasoning at each step and include examples",
 
)
result = Runner.run_sync(agent, "Write a haiku about recursion in programming.", run_config=config)
print(result.final_output)
