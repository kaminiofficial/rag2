import streamlit as st
from assistant.pipeline import  build_assistant, ask_question
from assistant.logger import get_logger

logger = get_logger(__name__)

st.title("Langchain Assistant")
st.write("Ask questions about the loaded data.")

@st.cache_resource(show_spinner='Loading the assistant...')
def load_assistant():
    logger.info("Loading the assistant...")
    assistant = build_assistant(data=None)  # Pass None to load data from the web
    logger.info("Assistant loaded successfully!")
    return assistant

assistant = load_assistant()    

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show the past conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get a new question from the user
question = st.chat_input("Ask a question about langchain...")

if question:
    logger.info("=== Streamlit run: new question received ===")
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = ask_question(assistant, question)
        st.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})