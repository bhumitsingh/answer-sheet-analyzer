from input_module.handler import process_input

print("=== TYPED TEXT TEST ===")
typed_answers = process_input("data/raw/typed_example.txt", "typed")
print(typed_answers)

print("\n=== MCQ TEST ===")
mcq_answers = process_input("data/raw/mcq_example.json", "mcq")
print(mcq_answers)

print("\n=== HANDWRITTEN OCR TEST ===")
handwritten_answers = process_input("data/raw/scan1.png", "handwritten")
print(handwritten_answers)
