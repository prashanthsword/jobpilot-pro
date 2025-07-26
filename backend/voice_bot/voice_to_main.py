from backend.voice_bot.speech_to_text import speech_to_text
from backend.voice_bot.text_to_speech import speak_text
from backend.llama_utils import get_llama_response

while True:
    try:
        user_input = speech_to_text()
        if user_input:
            print(f"🗣️ You said: {user_input}")
            response = get_llama_response(user_input)
            print(f"🤖 LLaMA Reply: {response}")
            speak_text(response)
        else:
            print("❌ Could not understand audio.")
    except KeyboardInterrupt:
        print("\n🛑 Voice bot terminated.")
        break
