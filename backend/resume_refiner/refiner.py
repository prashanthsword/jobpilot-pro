import subprocess
import tempfile

def generate_resume_improvements_llama(resume_text, jd_text):
    prompt = f"""
You are an ATS resume assistant. Review the following resume and job description, then list 5 specific improvements.

### RESUME
{resume_text}

### JOB DESCRIPTION
{jd_text}

### INSTRUCTIONS
Respond only with numbered improvement suggestions.
"""

    with tempfile.NamedTemporaryFile(delete=False, mode="w", suffix=".txt", encoding="utf-8") as temp_file:
        temp_file.write(prompt)
        temp_path = temp_file.name

    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt,
        text=True,
        capture_output=True
    )

    return result.stdout.strip()
