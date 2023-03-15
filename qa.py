import openai
import os
from joblib import Memory

# Set up the OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Set up caching
memory = Memory(location="cache", verbose=0)

# Create a function to ask a question
@memory.cache
def ask_question(question):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Q: {question}\nA:",
            temperature=0.5,
            max_tokens=100,
            n=1,
            stop=None,
            timeout=10,
        )

        answer = response.choices[0].text.strip()
        return answer
    except Exception as e:
        print(f"Error: {e}")
        return None

# Run the program in a loop
while True:
    try:
        # Ask a question from the terminal
        question = input("\nEnter your question (or 'exit' to quit): ")
        
        # Check if the user wants to exit
        if question.lower() == "exit":
            print("\nExiting...")
            break
        
        # Get the answer to the question
        answer = ask_question(question)

        # Print the answer
        if answer:
            print(f"\nQ: {question}\nA: {answer}")
        else:
            print(f"\nSorry, I couldn't find an answer to your question.")
    
    except KeyboardInterrupt:
        print("\nExiting...")
        break
