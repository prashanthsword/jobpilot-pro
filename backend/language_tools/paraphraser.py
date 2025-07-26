from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("Vamsi/T5_Paraphrase_Paws")
model = T5ForConditionalGeneration.from_pretrained("Vamsi/T5_Paraphrase_Paws")

def paraphrase_text(text: str) -> str:
    if len(text.strip()) < 10:
        return "❌ Text too short to paraphrase."

    input_text = f"paraphrase: {text} </s>"
    input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=256, truncation=True)
    output_ids = model.generate(
        input_ids,
        max_length=100,
        num_beams=4,
        do_sample=True,
        top_k=120,
        top_p=0.95,
        early_stopping=True
    )

    return tokenizer.decode(output_ids[0], skip_special_tokens=True)
