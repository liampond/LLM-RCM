# LLM-RCM

This repository accompanies the paper *Teaching LLMs Music Theory with In-Context Learning and Chain-of-Thought Prompting: Pedagogical Strategies for Machines*, which explores how large language models (LLMs) like ChatGPT, Claude, and Gemini can be taught to reason about music theory using in-context learning and chain-of-thought prompting. The study systematically evaluates model performance on Royal Conservatory of Music (RCM) Level 6 theory exam questions encoded in ABC, Humdrum, MEI, and MusicXML formats.

The paper was published and presented at the 17th International Conference on Computer Supported Music Education (CSME/CSEDU 2025) in Porto, Portugal, on April 3, 2025. DOI: [10.5220/0013506100003932](https://doi.org/10.5220/0013506100003932)

Pond, Liam, and Ichiro Fujinaga. 2025. “Teaching LLMs Music Theory with In-Context Learning and Chain-of-Thought Prompting: Pedagogical Strategies for Machines.” In *Proceedings of the 17th International Conference on Computer Supported Education (CSEDU 2025)* 1: 671–81. ISBN 978-989-758-746-7.

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/liampond/LLM-RCM.git
   cd LLM-RCM
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Add your API keys:**

   Create a `.env` file in the root directory with your API credentials. Do not share your API keys with anyone and do not commit the .env file to GitHub.

   ```
   CHATGPT_API_KEY=your-openai-api-key
   CLAUDE_API_KEY=your-anthropic-api-key
   GEMINI_API_KEY=your-gemini-api-key
   DEEPSEEK_API_KEY=your-deepseek-api-key
   ```

## Usage

### Run a Single Prompt

Use `main.py` to run a specific question for one model:

```bash
python main.py \
  --exam RCM6 \
  --context Context \
  --datatype MEI \
  --question Q4b \
  --model Claude \
  --examdate August2024
```

**Arguments:**

| Argument     | Description                                       |
|--------------|---------------------------------------------------|
| `--exam`     | Exam level (`RCM5` or `RCM6`)                     |
| `--context`  | Prompt type (`Context` or `NoContext`)            |
| `--datatype` | File format (`ABC`, `MEI`, `HumDrum`, `MusicXML`) |
| `--question` | Question code (e.g. `Q4b`, `Q7ai`)                 |
| `--model`    | `ChatGPT`, `Claude`, `Gemini`, or `DeepSeek`      |
| `--examdate` | (Optional) Exam date string (default: `August2024`) |

Output files will be saved to:
```
outputs/{MODEL}/{RCM_LEVEL}/{CONTEXT}/{DATATYPE}/{QUESTION}_..._Output.{ext}
```

### Run All Prompts in Batch

Use `batch_runner.py` to automatically run all questions for a given model:

```bash
python batch_runner.py \
  --model Claude \
  --exam RCM6 \
  --context Context \
  --examdate August2024
```

This will run every supported RCM6 question across all four data formats (ABC, HumDrum, MEI, MusicXML).

Note: Only RCM6 is currently supported in batch mode.

## File Structure

| Path                        | Purpose                                         |
|-----------------------------|-------------------------------------------------|
| `main.py`                   | Runs a single prompt                            |
| `batch_runner.py`           | Runs a batch of prompts                         |
| `config/settings.py`        | Model defaults and API key loading              |
| `prompts/`                  | Prompt templates used in experiments            |
| `EncodedFiles/`             | Input music files (by format and exam level)    |
| `outputs/`                  | Saved responses from LLMs                       |
| `.env`                      | (User-created) Stores your API keys securely    |
