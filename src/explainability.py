def generate_explanation(candidate):

    explanation = []

    if candidate['semantic_score'] > 0.40:
        explanation.append(
            "Good alignment with job description"
        )

    if candidate['leadership'] > 0:
        explanation.append(
            "Shows leadership indicators"
        )

    if candidate['innovation'] > 0:
        explanation.append(
            "Demonstrates innovation mindset"
        )

    return explanation