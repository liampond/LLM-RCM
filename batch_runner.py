import os
import subprocess
from settings import EXAM, CONTEXT, MODEL, EXTENSION_MAP

# Define all data types
DATA_TYPES = ["ABC", "MEI", "HumDrum", "MusicXML"]

# Define the path to the main script
MAIN_SCRIPT = "main.py"

def run_main_script(datatype, question):
    # Set the environment variables for each run
    os.environ["DATATYPE"] = datatype
    os.environ["QUESTION"] = question

    # Execute the main script
    subprocess.run(["python", MAIN_SCRIPT])

def get_all_questions(exam, context):
    # Path to the prompts folder
    prompt_dir = os.path.join("prompts", exam, context)
    
    # List all question prompt files
    return [f.split("_")[2] for f in os.listdir(prompt_dir) if f.endswith("Prompt.txt")]

def batch_run(exam, context, datatype=None):
    # Get all questions for the given exam and context
    questions = get_all_questions(exam, context)
    
    datatypes_to_run = [datatype] if datatype else DATA_TYPES
    
    for dt in datatypes_to_run:
        for question in questions:
            print(f"Running {exam} {context} {dt} {question}")
            run_main_script(dt, question)

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
