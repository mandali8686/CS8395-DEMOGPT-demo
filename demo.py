import streamlit as st
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (ChatPromptTemplate,
                                    HumanMessagePromptTemplate,
                                    SystemMessagePromptTemplate)
from langchain.document_loaders import *
from langchain.chains.summarize import load_summarize_chain
import tempfile
from langchain.docstore.document import Document

st.title("Feature Extraction")

# Initialize state variables
description = st.text_area("Enter the description paragraph for application design")
features = ""

# Function to extract features from description
def featureExtractor(description):
    chat = ChatOpenAI(
        model="gpt-3.5-turbo-16k",
        temperature=0
    )
    system_template = """You are an assistant tasked with extracting the features needed for an application from the given description paragraph."""
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    human_template = """Please extract the features required for the application from the following description: '{description}'."""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    result = chain.run(description=description)
    return result # returns string   

# Get input from the user
if st.button("Submit"):
    if description:
        features = featureExtractor(description)

# Display the extracted features to the user
st.markdown("Extracted Features:")
st.markdown(features)