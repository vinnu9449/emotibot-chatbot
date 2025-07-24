
import streamlit as st
from transformers import pipeline
from gtts import gTTS
import os

st.title("🎭 EmotiBot - Emotion-Based Chat Companion")
st.write("Talk to me! I’ll detect your emotion and reply with empathy.")

emotion_model = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion", top_k=1)

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:")

def generate_response(user_input):
    prediction = emotion_model(user_input)[0][0]  # Access inner dict
    label = prediction['label']
    responses = {
        "joy": "Yay! That’s great to hear 😊",
        "sadness": "I’m here for you. Wanna talk? 💙",
        "anger": "Take a deep breath. You’ve got this 💪",
        "fear": "Don’t worry, you’re not alone 🫂",
        "love": "Aww, that’s sweet! ❤️",
        "surprise": "Whoa! That’s unexpected! 😲",
        "neutral": "Tell me more! I’m all ears 👂"
    }
    return responses.get(label, "I’m not sure how to respond... but I’m listening!")

if user_input:
    response = generate_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))
    st.markdown(f"**Bot:** {response}")

st.markdown("### Chat History:")
for speaker, msg in st.session_state.chat_history:
    st.write(f"**{speaker}:** {msg}")
