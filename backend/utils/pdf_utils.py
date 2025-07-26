from fpdf import FPDF

def save_cover_letter_to_pdf(text, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Handle encoding safely
    for line in text.split("\n"):
        try:
            pdf.multi_cell(0, 10, line.encode('latin-1', 'replace').decode('latin-1'))
        except Exception as e:
            pdf.multi_cell(0, 10, "⚠️ Error encoding this line.")

    pdf.output(filename)
