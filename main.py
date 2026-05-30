import os
import pandas as pd

from src.parser import extract_text, extract_skills
from src.embeddings import semantic_similarity
from src.behavior_engine import score_behavior
from src.ranking import calculate_final_score
from src.explainability import generate_explanation

JOB_DESCRIPTION = open(
    'data/jobs/job.txt',
    encoding='utf-8'
).read()

results = []

resume_folder = 'data/resumes/'

print(os.listdir(resume_folder))

for file in os.listdir(resume_folder):

    path = os.path.join(resume_folder, file)

    text = extract_text(path)

    skills = extract_skills(text)

    semantic = semantic_similarity(
        JOB_DESCRIPTION,
        text
    )

    behavior = score_behavior(text)

    behavior_avg = (
        sum(behavior.values()) /
        len(behavior)
    )

    skill_score = len(skills) / 10

    trajectory_score = 0.7
    project_score = 0.8
    growth_score = 0.7

    if 'python' in skills and 'sql' in skills:
        growth_score += 0.1

    final_score = calculate_final_score(
        semantic,
        skill_score,
        trajectory_score,
        behavior_avg / 10,
        project_score,
        growth_score
    )

    explanation = generate_explanation({

        'semantic_score': semantic,

        'leadership': behavior['leadership'],

        'innovation': behavior['innovation']
    })

    results.append({

        'candidate': file,

        'score': final_score,

        'skills': ", ".join(skills),

        'explanation': " | ".join(explanation)
    })

results = sorted(
    results,
    key=lambda x: x['score'],
    reverse=True
)

output = pd.DataFrame(results)

output.to_csv(
    'data/outputs/ranked_candidates.csv',
    index=False
)

print(output)