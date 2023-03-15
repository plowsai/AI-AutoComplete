# first line: 12
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
