from random import sample
import streamlit as st
from templates.template_html import flashcard_template, flashcard_script, css

def generate_flashcards(text_chunks, llm, num_flashcards=5):
    """Genereaza intrebari pe baza LLM-ului si creeaza flashcards."""
    flashcards = []
    for chunk in text_chunks:
        prompt_for_question = f"Please generate a unique question based on this text:\n\n{chunk}"
        question_response = llm(prompt_for_question)
        question = question_response.strip()

        prompt_for_answer = f"Based on the question '{question}', please provide an answer using the following text:\n\n{chunk}"
        answer_response = llm(prompt_for_answer)
        answer = answer_response.strip()

        flashcards.append({"question": question, "answer": answer})
        if len(flashcards) >= num_flashcards:
            break
    return flashcards
def display_flashcard(card, key):
    st.markdown(flashcard_template.replace("{{QUESTION}}", card["question"]).replace("{{ANSWER}}", card["answer"]).replace("{{KEY}}", str(key)), unsafe_allow_html=True)
    st.markdown(flashcard_script, unsafe_allow_html=True)
