import subprocess
import argparse

# List of all questions to iterate through
RCM5_QUESTIONS = [] # TODO
RCM6_QUESTIONS = ["Q1a", "Q6i", "Q6ii", "Q7ai", "Q7aii", "Q7aiii", "Q7b", "Q9a", "Q9b", "Q10"]

#ALL_QUESTIONS = ["Q1a", "Q1b", "Q2a", "Q2b", "Q3a", "Q3b", "Q3c", "Q3d", "Q3e", "Q4a", "Q4b", "Q5",
#              "Q6i", "Q6ii", "Q7ai", "Q7aii", "Q7aiii", "Q7b", "Q9a", "Q9b", "Q10"]

DATATYPES = ["ABC", "HumDrum", "MEI", "MusicXML"]

def run_batch(model, exam, context, examdate):
    for question in RCM6_QUESTIONS:
        for datatype in DATATYPES:
            # Command to run main.py with dynamic arguments
            command = [
                "python", "main.py",
                "--exam", exam,
                "--context", context,
                "--datatype", datatype,
                "--question", question,
                "--model", model,
                "--examdate", examdate
            ]

            # Display the command for tracking
            print(f"▶️ Running: {' '.join(command)}")

            # Run the command
            subprocess.run(command)

if __name__ == "__main__":
    #Example call: python batch_runner.py --exam RCM6 --context Context --model Claude --examdate August2024
    parser = argparse.ArgumentParser(description="Batch runner for multiple questions and datatypes.")
    parser.add_argument('--model', type=str, default="ChatGPT", help='Model to use (ChatGPT, Claude, DeepSeek, Gemini), default: ChatGPT')
    parser.add_argument('--exam', type=str, default="RCM6", help='Exam level (default: RCM6)')
    parser.add_argument('--context', type=str, default="NoContext", help='Context (default: NoContext)')
    parser.add_argument('--examdate', type=str, default="August2024", help='Exam date (default: August2024)')

    args = parser.parse_args()

    run_batch(args.model, args.exam, args.context, args.examdate)
