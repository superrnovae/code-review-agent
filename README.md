# AI Code Review Agent

## Objective
Build a local or prompt-based AI agent that can analyze Python code, detect potential issues, suggest improvements, and act like a code reviewer.

## Project Structure
```
code_review_agent/
├── agent/
│   ├── analyzer.py
│   └── llm_interface.py
├── examples/
│   ├── buggy_script.py
│   └── clean_script.py
├── prompts/
│   └── templates.yaml
├── reviews/
│   └── review_output.md
├── cli.py
├── config.yaml
├── README.md
└── requirements.txt
```

## Usage
1. Export API keys:
   ```bash
   export OPENAI_API_KEY='...'
   export ANTHROPIC_API_KEY='...'
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run a review:
   ```bash
   python cli.py --file examples/buggy_script.py --mode strict --provider openai
   ```
