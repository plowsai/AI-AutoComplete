import os
import sys
import openai
import requests

# Replace with your OpenAI API key
api_key = "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"
openai.api_key = api_key

def correct_command(command):
    prompt = f"Rewrite the following incorrectly typed terminal command into a correctly typed command: '{command}'"
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )

    corrected_command = response.choices[0].text.strip()

    if not corrected_command:
        print(f"No corrected command found. Executing the original command: {command}", file=sys.stderr)
        return command

    return corrected_command


def main():
    command = sys.stdin.read().strip()
    corrected_command = correct_command(command)
    print(corrected_command)

if __name__ == "__main__":
    main()
