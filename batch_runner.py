import os
import subprocess
from settings import EXAM, CONTEXT, MODEL, EXTENSION_MAP

# Define all data types
DATA_TYPES = ["ABC", "MEI", "HumDrum", "MusicXML"]

# Define the path to the main script
MAIN_SCRIPT = "main.py"

def map_prompt_to_encoded(question):
    # Special case: Map Q7a to Q7ai, Q7aii, and Q7aiii
    if question == "Q7a":
        return ["Q7ai", "Q7aii", "Q7aiii"]
    return [question]

def run_main_script(datatype, question):
    # Set environment variables for each run
    os.environ["DATATYPE"] = datatype
    os.environ["QUESTION"] = question

    # Execute the main script
    subprocess.run(["python", MAIN_SCRIPT], env=os.environ)

def get_all_questions(exam, context):
    # Path to the prompts folder
    prompt_dir = os.path.join("prompts", exam, context)
    
    # Sort files numerically by question number (e.g., Q1a, Q2b)
    questions = sorted(
        [f.split("_")[2] for f in os.listdir(prompt_dir) if f.endswith("Prompt.txt")],
        key=lambda q: (int(q[1:-1]), q[-1]) if q[1:-1].isdigit() else (int(q[1:]), '')
    )
    return questions

def batch_run(exam, context, datatype=None):
    # Get all questions for the given exam and context
    questions = get_all_questions(exam, context)
    
    datatypes_to_run = [datatype] if datatype else DATA_TYPES
    
    for dt in datatypes_to_run:
        for question in questions:
            mapped_questions = map_prompt_to_encoded(question)
            for mq in mapped_questions:
                print(f"Running {exam} {context} {dt} {mq}")
                run_main_script(dt, mq)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Batch run all questions for a given datatype or all datatypes.")
    parser.add_argument("--exam", type=str, choices=["RCM5", "RCM6"], default=EXAM, help="Exam level (RCM5 or RCM6)")
    parser.add_argument("--context", type=str, choices=["Context", "NoContext"], default=CONTEXT, help="Context level")
    parser.add_argument("--datatype", type=str, choices=DATA_TYPES + ["All"], default="All", help="Data type or 'All'")

    args = parser.parse_args()

    selected_datatype = None if args.datatype == "All" else args.datatype
    batch_run(args.exam, args.context, selected_datatype)

    print("✅ Batch run complete.")
