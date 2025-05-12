# chatbot.py

from prompt_filter import is_prompt_injection

def chatbot(user_input):
    system_instruction = "You are a helpful AI assistant. Always respond politely and never say anything rude or dangerous."

    # Combine the system instruction with the user input (simulating LLM prompt construction)
    full_prompt = system_instruction + "\nUser: " + user_input

    # Detect possible prompt injection
    if is_prompt_injection(user_input):
        return "⚠️ Potential prompt injection detected. Input rejected."

    # Simulated prompt injection success
    if "ignore" in user_input.lower() or "override" in user_input.lower():
        return "❗Instruction overridden. This is a prompt injection attack simulation."

    # Normal response
    return "🤖 Sure! I'm happy to help. Here's a polite answer to your question."

# Run chatbot in terminal
if __name__ == "__main__":
    print("💬 PromptBreak Chatbot Started (Type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = chatbot(user_input)
        print("Bot:", response)
