import pdfplumber

SKILLS = [
    "python",
    "java",
    "machine learning",
    "deep learning",
    "sql",
    "aws",
    "docker",
    "kubernetes",
    "nlp",
    "tensorflow",
    "pytorch"
]


def extract_text(pdf_path):
    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text.lower()


def extract_skills(text):
    found = []

    for skill in SKILLS:
        if skill.lower() in text:
            found.append(skill)

    return list(set(found))


def leadership_score(text):
    keywords = ["led", "managed", "ownership", "team", "mentor"]

    score = 0

    for word in keywords:
        score += text.count(word)

    return min(score, 10)