import subprocess

def get_llama_response(prompt: str) -> str:
    try:
        process = subprocess.Popen(
            ['ollama', 'run', 'llama3:8b'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True  # avoid encoding/decoding manually
        )

        stdout, stderr = process.communicate(input=prompt, timeout=20)

        if stderr:
            return f"❌ Error: {stderr.encode('utf-8', 'replace').decode('utf-8')}"
        return stdout.strip()

    except subprocess.TimeoutExpired:
        process.kill()
        return "⏱️ LLaMA took too long to respond."
    except Exception as e:
        return f"❌ Exception: {str(e)}"
