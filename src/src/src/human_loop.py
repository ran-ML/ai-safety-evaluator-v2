import csv
import os

FILE_PATH = "evaluation_log.csv"

def save_feedback(text, ai_result, human_agree):

    file_exists = os.path.isfile(FILE_PATH)

    with open(FILE_PATH, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "text",
                "harm_score",
                "bias_score",
                "fairness_score",
                "confidence",
                "ai_human_review_flag",
                "human_agree"
            ])

        writer.writerow([
            text,
            ai_result["harm_score"],
            ai_result["bias_score"],
            ai_result["fairness_score"],
            ai_result["confidence"],
            ai_result["human_review"],
            human_agree
        ])
