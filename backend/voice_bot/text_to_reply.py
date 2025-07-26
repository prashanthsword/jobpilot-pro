import subprocess

# Maintain conversation memory (simple list for now)
conversation_history = []

def get_llm_reply(user_input):
    system_prompt = (
        "You are Jarvis, a witty, highly intelligent AI assistant. "
        "Respond confidently, concisely, and conversationally like Tony Stark's AI. "
        "Always stay professional, never say you're an AI model. Use light humor if appropriate."
    )

    # Format history
    full_prompt = system_prompt + "\n\n"
    for turn in conversation_history[-5:]:  # Keep last 5 turns
        full_prompt += f"User: {turn['user']}\nJarvis: {turn['jarvis']}\n"
    full_prompt += f"User: {user_input}\nJarvis:"

    try:
        result = subprocess.run(
            ["ollama", "run", "llama3", full_prompt],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        response = result.stdout.strip()

        # Store in memory
        conversation_history.append({"user": user_input, "jarvis": response})

        return response
    except subprocess.CalledProcessError as e:
        print("⚠️ Ollama Error:", e.stderr)
        return "I'm experiencing a glitch. Maybe try again?"
