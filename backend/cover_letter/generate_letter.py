# backend/cover_letter/generate_letter.py

import subprocess

def generate_cover_letter(resume_text, job_description):
    print("🧠 Generating cover letter locally with LLaMA3...")

    prompt = f"""You are an AI career assistant. Based on the following RESUME and JOB DESCRIPTION, generate a professional and ATS-friendly cover letter.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

COVER LETTER:
"""

    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    output = result.stdout.decode("utf-8")
    return output.strip()
