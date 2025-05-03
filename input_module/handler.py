# input_module/handler.py

from .typed_parser import parse_typed_text
from .mcq_reader import parse_mcq_answers
from .ocr_extractor import extract_handwritten_text

def process_input(file_path: str, input_type: str):
    """
    Routes the input file to the correct parser based on type.

    :param file_path: Path to the input file.
    :param input_type: One of 'typed', 'mcq', 'handwritten'
    :return: Structured answer data (dict).
    """
    if input_type == "typed":
        return parse_typed_text(file_path)
    elif input_type == "mcq":
        return parse_mcq_answers(file_path)
    elif input_type == "handwritten":
        return extract_handwritten_text(file_path)
    else:
        raise ValueError(f"Unsupported input type: {input_type}")
