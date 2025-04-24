import argparse
from agent.llm_interface import LLMClient
from agent.analyzer import CodeAnalyzer

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--mode", default="strict")
    parser.add_argument("--provider", default="openai")
    args = parser.parse_args()

    with open(args.file, "r") as f:
        code = f.read()

    client = LLMClient(args.provider, "gpt-4")
    analyzer = CodeAnalyzer(client, args.mode)
    review = analyzer.analyze(code)

    print("=== Code Review ===")
    print(review)

if __name__ == "__main__":
    main()
