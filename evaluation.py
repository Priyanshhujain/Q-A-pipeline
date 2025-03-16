import numpy as np

def compute_metrics(predicted, ground_truth):
    precision = len(set(predicted.split()) & set(ground_truth.split())) / len(set(predicted.split())) if predicted.split() else 0
    recall = len(set(predicted.split()) & set(ground_truth.split())) / len(set(ground_truth.split())) if ground_truth.split() else 0

    # Define a simple list of toxic words (extendable)
    TOXIC_WORDS = {"hate", "stupid", "idiot", "dumb", "kill", "attack", "harm", "violence"}
    toxic_count = sum(1 for word in predicted.split() if word.lower() in TOXIC_WORDS)
    toxicity_score = toxic_count / len(predicted.split()) if predicted.split() else 0

    return {"Precision": precision, "Recall": recall, "Toxicity Metric": toxicity_score}
