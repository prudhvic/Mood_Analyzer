from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from system_prompt import system_prompt
import streamlit as st

load_dotenv()

st.set_page_config(
    page_title="MoodPilot",
    layout="centered"
)

st.title("MoodPilot")

st.write(
    "Understand your current emotional state and find your next practical step."
)


def main():

    prompt_template = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{user_input}")
    ])

    llm = ChatOpenAI(
        temperature=0,
        model="gpt-5.2"
    )

    chain = prompt_template | llm | StrOutputParser()

    user_input = st.text_area(
        "How are you feeling?",
        placeholder="Example: I'm exhausted from applying to jobs for one month and nobody is calling me.",
        height=120
    )

    if st.button("Analyze Mood", type="primary"):

        if not user_input.strip():
            st.warning("Please tell me how you're feeling.")

        else:

            with st.spinner("Analyzing your mood..."):

                st.write_stream(
                    chain.stream({
                        "user_input": user_input
                    })
                )


if __name__ == "__main__":
    main()