import chainlit as cl
from agents import Agent, Runner 
from agentsdk_gemini_adapter import config

@cl.on_message
async def main(message: cl.Message):
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant."
    )
    result = await Runner.run(agent, message.content , run_config=config)
    await cl.Message(content=result.final_output).send()
