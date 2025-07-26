from backend.interview_agent.agent import generate_interview_questions

resume_text = """
Recent graduate with experience in Python, machine learning, and web development. Built projects like resume matchers, emotion-based chatbots, and data dashboards.
"""

job_description = """
We are hiring for a Machine Learning Engineer with proficiency in Python, LLMs, and experience in deploying NLP models in production.
"""

questions = generate_interview_questions(resume_text, job_description)

print("\n🎯 Generated Interview Questions:\n")
print(questions)
