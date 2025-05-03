# input_module/mcq_reader.py

import csv
import json

def parse_mcq_answers(file_path: str) -> dict:
    """
    Parses MCQ answers from a CSV or JSON file.

    CSV Format:
    question_id,selected_option

    JSON Format:
    {"Q1": "A", "Q2": "C", ...}

    :param file_path: Path to file.
    :return: Dictionary of MCQ answers.
    """
    if file_path.endswith('.json'):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    elif file_path.endswith('.csv'):
        answers = {}
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                qid, answer = row
                answers[qid.strip()] = answer.strip()
        return answers
    
    else:
        raise ValueError("Only .csv and .json formats are supported for MCQs.")
