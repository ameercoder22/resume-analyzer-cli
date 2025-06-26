import fitz  # PyMuPDF
import argparse

KEYWORDS = ["Python", "Java", "SQL", "Machine Learning", "Data Analysis", "Git", "Flask", "React"]

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def analyze_resume(text):
    print("\n--- Skill Match Report ---")
    found_skills = []
    for skill in KEYWORDS:
        count = text.lower().count(skill.lower())
        if count > 0:
            print(f"{skill}: {count}")
            found_skills.append(skill)
        else:
            print(f"{skill}: ❌ Not found")
    
    print("\n--- Suggestions ---")
    missing = [skill for skill in KEYWORDS if skill not in found_skills]
    if missing:
        print("Consider adding these skills to make your resume stronger:")
        for skill in missing:
            print(f"- {skill}")
    else:
        print("Awesome! Your resume includes all the key skills.")

def main():
    parser = argparse.ArgumentParser(description="Analyze resume for tech skills.")
    parser.add_argument("pdf_path", help="Path to the resume PDF file")
    args = parser.parse_args()

    print(f"🔍 Reading from: {args.pdf_path}")
    text = extract_text_from_pdf(args.pdf_path)

    if not text.strip():
        print("⚠️ No extractable text found in the PDF.")
        print("❓ Is the resume scanned or image-based?")
        return

    print("✅ PDF text was extracted successfully.\n")
    print("----- Preview of Text (First 500 chars) -----")
    print(text[:500])
    print("---------------------------------------------\n")

    analyze_resume(text)

if __name__ == "__main__":
    main()
