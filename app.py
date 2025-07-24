import streamlit as st
from transformers import pipeline

# Load the emotion detection model
emotion_model = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

# Function to generate chatbot response
def generate_response(user_input):
    predictions = emotion_model(user_input)
    label = predictions[0]['label']

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

# Initialize session state for storing chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Title
st.title("💬 Emotion Chatbot")
st.write("Talk to me and I’ll respond based on how you feel!")

# Input form for Enter key submission
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", "", placeholder="Type your message here and press Enter")
    submitted = st.form_submit_button("Send")  # Hidden default button

if submitted and user_input.strip():
    # Add user message to history
    st.session_state.messages.append(("You", user_input))

    # Generate and store bot response
    bot_response = generate_response(user_input)
    st.session_state.messages.append(("Bot", bot_response))

# Display chat history
for sender, msg in st.session_state.messages:
    if sender == "You":
        st.markdown(f"**🧍‍♂️ You:** {msg}")
    else:
        st.markdown(f"**🤖 Bot:** {msg}")
