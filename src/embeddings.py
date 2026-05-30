from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')


def get_embedding(text):
    return model.encode([text])[0]


def semantic_similarity(job_text, resume_text):

    job_emb = get_embedding(job_text)
    resume_emb = get_embedding(resume_text)

    score = cosine_similarity(
        [job_emb],
        [resume_emb]
    )[0][0]

    return float(score)