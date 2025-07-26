def get_interview_prompt(resume_text: str, job_description: str) -> str:
    return f"""
    Act as a virtual interviewer. Based on the resume and job description below, generate 5 relevant technical interview questions.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Format the questions as a numbered list.
    """
