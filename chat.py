import streamlit as st
import time

# Custom CSS for styling
st.markdown(
    """
    <style>
    .thinking-message {
        font-size: 24px;
        color: #ff4500;
        font-weight: bold;
        text-align: center;
    }
    .header {
        text-align: center;
        font-size: 36px;
        color: #2E8B57;
        margin-bottom: 20px;
    }
    .question {
        text-align: center;
        font-size: 20px;
    }
    .answer {
        text-align: center;
        font-size: 24px;
        color: #1E90FF;
    }
    </style>
    """, unsafe_allow_html=True
)

# Title of the app with custom header styling
st.markdown('<div class="header">Becode Chatbot</div>', unsafe_allow_html=True)

# Ask a question to the chatbot with custom styling
user_question = st.text_input("Ask me anything:")

# Create a submit button for user interaction
submit_button = st.button("Submit")

# Logic to respond with a Rickroll GIF and the image of the person after some "thinking" time
if submit_button and user_question:
    st.markdown('<div class="question">Hmm... let me think about that...</div>', unsafe_allow_html=True)
    
    # Create a placeholder for the thinking animation (simulated by text here)
    thinking_placeholder = st.empty()
    
    # Simulate "thinking" by showing a timer or "brainstorming" message
    for i in range(3, 0, -1):  # Simulate a countdown of 3 seconds
        thinking_placeholder.markdown(f'<div class="thinking-message">Thinking... {i} ⏳</div>', unsafe_allow_html=True)
        time.sleep(1)  # Wait for 1 second
    
    # Clear the placeholder
    thinking_placeholder.empty()
    
    # Directly show the Rickroll GIF with custom styling for the answer
    st.markdown('<div class="answer">Ah, I\'ve got it! Here\'s your answer:</div>', unsafe_allow_html=True)
    
    # Display the image of the person (replace 'your_image.png' with the actual file name)
    st.image('background.jpg', caption='Surprise!', use_column_width=True)  # Ensure the file is in the same directory

