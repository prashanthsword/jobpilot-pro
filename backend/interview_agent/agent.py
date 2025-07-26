import subprocess

from backend.interview_agent.prompts import get_interview_prompt

def generate_interview_questions(resume_text: str, job_description: str) -> str:
    print("🤖 Generating interview questions with LLaMA...")
    
    prompt = get_interview_prompt(resume_text, job_description)

    # Use llama3 via subprocess (ollama run llama3)
    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt,
        capture_output=True,
        text=True
    )

    return result.stdout.strip()
