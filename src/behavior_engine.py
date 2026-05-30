TRAITS = {
    "leadership": [
        "led",
        "managed",
        "mentored",
        "ownership"
    ],

    "collaboration": [
        "team",
        "collaborated",
        "cross-functional"
    ],

    "innovation": [
        "built",
        "created",
        "developed",
        "designed"
    ],

    "adaptability": [
        "learned",
        "adapted",
        "transitioned"
    ]
}


def score_behavior(text):

    scores = {}

    for trait, words in TRAITS.items():

        count = 0

        for word in words:
            count += text.count(word)

        scores[trait] = min(count, 10)

    return scores