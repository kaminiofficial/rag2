from assistant.pipeline import ask_question, build_assistant
from assistant.logger import get_logger

logger = get_logger(__name__)

def main():
    logger.info("Building the assistant...")
    assistant = build_assistant(data=None)  # Pass None to load data from the web
    logger.info("Assistant built successfully!")

    questions=("who created langchain?","when to use langraph?","how to use jina embeddings?")

    for question in questions:
        logger.info(f"Asking question: {question}")
        answer = ask_question(assistant, question)
        logger.info(f"Answer: {answer}")

if __name__ == "__main__":
    main()
