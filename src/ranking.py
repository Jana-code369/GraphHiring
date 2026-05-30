def calculate_final_score(
    semantic_score,
    skill_score,
    trajectory_score,
    behavior_score,
    project_score,
    growth_score
):

    final_score = (
        semantic_score * 0.30 +
        skill_score * 0.20 +
        trajectory_score * 0.15 +
        behavior_score * 0.20 +
        project_score * 0.10 +
        growth_score * 0.05
    )

    return round(final_score * 100, 2)