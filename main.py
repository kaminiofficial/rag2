from assistant.pipeline import ask_question, build_assistant

def main():
    print("Building the assistant...")
    assistant = build_assistant(data=None)  # Pass None to load data from the web
    print("Assistant built successfully!")

    questions=['what is langchain?','what is groq?','what is jina?']

    for question in questions:
        print(f"Asking question: {question}")
        answer = ask_question(assistant, question)
        print(f"Answer: {answer}")

if __name__ == "__main__":
    main()
