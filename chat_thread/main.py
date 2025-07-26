from agents import Agent, Runner, Session, SQLiteSession
from agentsdk_gemini_adapter import config

agent = Agent(
    name="ChatAgent",
    instructions=(
        "Tum aik Urdu conversational assistant ho. "
        "User ke har sawal ka jawab dena ha aur pehli baat cheet yaad rakhni ha."
    )
)

def manual_chat():
    print("\n📘 Manual History Mode (You manage history)")
    history = []

    while True:
        user_input = input("👤 You: ")
        if user_input.lower() == "exit":
            break

        history.append({"role": "user", "content": user_input})
        result = Runner.run_sync(agent, history , run_config=config)
        print("🤖 Agent:", result.final_output)
        history = result.to_input_list() 

def automatic_chat():
    print("\n📗 Automatic Session Mode (Agent remembers context)")
    session = SQLiteSession("my_chat_session")  

    while True:
        user_input = input("👤 You: ")
        if user_input.lower() == "exit":
            break
        result = Runner.run_sync(agent, user_input, session=session , run_config=config)
        print("🤖 Agent:", result.final_output)

if __name__ == "__main__":
    print("Choose mode:")
    print("1 - Manual history")
    print("2 - Automatic session")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        manual_chat()
    elif choice == "2":
        automatic_chat()
    else:
        print("❌ Invalid choice. Exiting.")
