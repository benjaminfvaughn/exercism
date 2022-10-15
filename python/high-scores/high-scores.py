def latest(scores):
    return scores[len(scores)-1]

def personal_best(scores):
    scores.sort(reverse=True)
    return scores[0]
    pass

def personal_top_three(scores):
    scores.sort(reverse=True)
    return scores[0:3]
    pass
