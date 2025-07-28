from dataclasses import dataclass
from agents import Agent, Runner, function_tool
from agentsdk_gemini_adapter import config

@dataclass
class UserContext:
    uid: str

    def get_user_plan(self) -> str:
        if self.uid == "1":
            return "Enterprise"
        elif self.uid == "2":
            return "Pro"
        elif self.uid == "3":
            return "Basic"
        else:
            return "Unknown"


@function_tool
def get_plan_for_current_user(context: UserContext) -> str:
    """
    Return the plan type for the current user.
    Uses context.uid to determine the plan.
    """
    return context.get_user_plan()


agent = Agent(
    name="UserPlanAgent",
    instructions="""
You are a subscription assistant. 
Your job is to determine the user's plan by calling the get_plan_for_current_user tool.
Do not guess. Always use the tool to retrieve the plan.
""",
    tools=[get_plan_for_current_user]
)


if __name__ == "__main__":
    context = UserContext(uid="1")  # Change this to test other IDs
    result = Runner.run_sync(agent, "What is the user's plan?", context=context , run_config=config)
    print("Final Output:", result.final_output)
