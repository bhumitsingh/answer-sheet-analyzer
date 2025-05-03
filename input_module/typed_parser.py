# input_module/typed_parser.py

def parse_typed_text(file_path: str) -> dict:
    """
    Reads and parses a typed text file containing student answers.

    Expected format:
    Q1: Answer one
    Q2: Answer two

    :param file_path: Path to the TXT file.
    :return: Dictionary with question IDs and answers.
    """
    answers = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if ":" in line:
                qid, ans = line.strip().split(":", 1)
                answers[qid.strip()] = ans.strip()
    return answers
