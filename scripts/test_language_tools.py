from backend.language_tools.grammar_corrector import correct_grammar
from backend.language_tools.summarizer import summarize_text
from backend.language_tools.paraphraser import paraphrase_text

sample_text = """
This are a bad sentence. It need more gooder grammar and clearly to be understand by peoples.
"""

print("✅ Grammar Corrected:\n", correct_grammar(sample_text))
print("\n📄 Summary:\n", summarize_text(sample_text))
print("\n🔁 Paraphrased:\n", paraphrase_text(sample_text))
