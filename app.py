import streamlit as st
from transformers import pipeline

# Load the emotion detection model
emotion_model = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

# Function to generate chatbot response
def generate_response(user_input):
    predictions = emotion_model(user_input)
    label = predictions[0]['label']  # Top emotion label

    responses = {
        "joy": "Yay! That’s great to hear 😊",
        "sadness": "I’m here for you. Wanna talk? 💙",
        "anger": "Take a deep breath. You’ve got this 💪",
        "fear": "Don’t worry, you’re not alone 🫂",
        "love": "Aww, that’s sweet! ❤️",
        "surprise": "Whoa! That’s unexpected! 😲",
        "neutral": "Tell me more! I’m all ears 👂"
    }

    return responses.get(label.lower(), "I’m not sure how to respond... but I’m listening!")

# Streamlit app UI
st.title("💬 Emotion Chatbot")
st.write("Talk to me and I’ll respond based on how you feel!")

# User input
user_input = st.text_input("You:", "")

# Generate and display response
if st.button("Send") or user_input:
    if user_input.strip() != "":
        bot_response = generate_response(user_input)
        st.text_area("Chatbot:", value=bot_response, height=100)
