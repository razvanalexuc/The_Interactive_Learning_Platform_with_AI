from streamlit.components.v1 import html
from templates.template_html import flashcard_script, css, flashcard_template
import streamlit as st

def flashcard_component(flashcard_data, key):
    html(
        f"""
        <div class="flashcard" id="flashcard-{key}">
            <div class="front">{flashcard_data['question']}</div>
            <div class="back">{flashcard_data['answer']}</div>
        </div>
        <button class="flip-button" onclick="flipCard({key})">Flip</button>
        {css}
        {flashcard_script}
        """,
        height=200, 
        scrolling=True
    )