import argparse
import os
from models.chatgpt_api import chatgpt_request
from models.claude_api import claude_request
from models.gemini_api import gemini_request
from utils.prompt_loader import load_prompt
from utils.encoded_file_loader import load_encoded_file
from utils.save_response import save_response
from config import settings

# Questions without encoded files
QUESTIONS_WITHOUT_ENCODED_FILES = ["Q3a", "Q3b", "Q3c", "Q3d", "Q3e", "Q5", "Q6", "Q9a", "Q9b"]

# Prompt Pathing
base_prompt_path = "prompts"
all_prompts = "AllPrompts"
encoded_files = "EncodedFiles"

def build_conversation(exam, context, datatype, question, examdate):
    # Build system prompt path
    system_prompt_path = os.path.join(base_prompt_path, all_prompts, "AllPromptsSystem.txt")
    system_prompt = load_prompt(system_prompt_path)

    # Build question prompt path
    question_prompt_path = os.path.join("prompts", exam, context, f"{exam}_{examdate}_{question}_{context}Prompt.txt")
    question_prompt = load_prompt(question_prompt_path)

    # If no encoded file is required
    if question in QUESTIONS_WITHOUT_ENCODED_FILES:
        conversation = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question_prompt}
        ]
    else:
        # Build datatype-specific prompt path
        datatype_prompt_path = os.path.join(base_prompt_path, all_prompts, f"AllPromptsUser_{datatype}.txt")
        datatype_prompt = load_prompt(datatype_prompt_path)

        # Build encoded file path
        file_extension = settings.EXTENSION_MAP[datatype]
        encoded_file_path = os.path.join(encoded_files, exam, datatype, f"{exam}_{examdate}_{question}{file_extension}")
        # Check if encoded file exists
        if not os.path.exists(encoded_file_path):
            print(f"⚠️ Skipping {question} due to missing encoded file: {encoded_file_path}")
            exit()
        encoded_file_content = load_encoded_file(encoded_file_path)

        # Build the full conversation
        conversation = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": datatype_prompt},
            {"role": "user", "content": f"Here is the encoded music file in {datatype} format:\n\n{encoded_file_content}"},
            {"role": "user", "content": question_prompt}
        ]

    return conversation

def call_model_api(model, conversation):
    if model == "ChatGPT":
        response = chatgpt_request(conversation, settings.CHATGPT_API_KEY)
    elif model == "Claude":
        response = claude_request(conversation, settings.CLAUDE_API_KEY)
    elif model == "Gemini":
        response = gemini_request(conversation, settings.GEMINI_API_KEY)
    else:
        raise ValueError("Invalid model selected!")
    return response

def main(exam, context, datatype, question, model, examdate):
    # Build the conversation prompt
    conversation = build_conversation(exam, context, datatype, question, examdate)

    # Call the model API
    response = call_model_api(model, conversation)

    # Extract and save the response
    response_content = "\n".join([choice.message.content.strip() for choice in response.choices])
    output_dir = os.path.join("outputs", model, exam, datatype)
    os.makedirs(output_dir, exist_ok=True)

    output_filename = f"{model}_{exam}_{examdate}_{question}_{context}_{datatype}_Output.txt"
    output_path = os.path.join(output_dir, output_filename)

    save_response(output_path, response_content)

    print(f"✅ {model} response for {question}, {model}, {exam}_{examdate}, {datatype}, {context} saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run prompt generation and model API call.")
    parser.add_argument('--exam', type=str, required=True, help='Exam level (RCM5 or RCM6)')
    parser.add_argument('--context', type=str, required=True, help='Context (Context or NoContext)')
    parser.add_argument('--datatype', type=str, required=True, help='Data type (ABC, MEI, HumDrum, MusicXML)')
    parser.add_argument('--question', type=str, required=True, help='Question number (e.g., Q1a)')
    parser.add_argument('--model', type=str, required=True, help='Model to use (ChatGPT, Claude, Gemini)')
    parser.add_argument('--examdate', type=str, default='August2024', help='Exam date (e.g., August2024)')

    args = parser.parse_args()
    main(args.exam, args.context, args.datatype, args.question, args.model, args.examdate)
