import streamlit as st
import re

# Page configuration
st.set_page_config(
    page_title='Password Strength Checker',
    page_icon='🔒',
    layout='centered',
    initial_sidebar_state='collapsed'
)

# Custom Styling
st.markdown(
    """
    <style>
        /* Background gradient animation */
        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        body {
            background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
        }
        .main {
            background: rgba(255, 255, 255, 0.9);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.2);
            margin: 20px auto;
            max-width: 600px;
        }
        h1 {
            color: white;
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 1rem;
            background: linear-gradient(45deg, #4CAF50, #23a6d5);
            padding: 1rem;
            border-radius: 10px;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
        }
        h2 {
            color: #555;
            text-align: center;
            font-size: 1.5rem;
            margin-bottom: 1.5rem;
        }
        .stTextInput>div>div>input {
            padding: 12px;
            border-radius: 8px;
            border: 1px solid #ccc;
            width: 100%;
            font-size: 16px;
        }
        .feedback {
            font-size: 16px;
            padding: 12px;
            border-radius: 8px;
            margin: 10px 0;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .feedback:hover {
            transform: translateY(-2px);
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2);
        }
        .strong {
            background-color: #d4edda;
            color: #155724;
            border-left: 5px solid #28a745;
        }
        .moderate {
            background-color: #fff3cd;
            color: #856404;
            border-left: 5px solid #ffc107;
        }
        .weak {
            background-color: #f8d7da;
            color: #721c24;
            border-left: 5px solid #dc3545;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 12px 24px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            width: 100%;
            font-size: 16px;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .info {
            background-color: #d1ecf1;
            color: #0c5460;
            border-left: 5px solid #17a2b8;
            padding: 12px;
            border-radius: 8px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Heading with gradient background
st.markdown(
    """
    <h1>🔒 Password Strength Checker</h1>
    """,
    unsafe_allow_html=True
)


st.markdown("## Enter your password to check its strength 🛡️")


password = st.text_input('Enter your password', type='password', placeholder='Type your password here...')
feedback = []
score = 0

if password:
   
    if len(password) < 8:
        feedback.append(('❌ Password should be at least 8 characters long.', 'weak'))
    else:
        score += 1

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append(('❌ Password should contain both uppercase and lowercase letters.', 'weak'))

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append(('❌ Password should contain at least one digit.', 'moderate'))

    if re.search(r'[@#$&]', password):
        score += 1
    else:
        feedback.append(('❌ Password should contain at least one special character (@, #, $, &).', 'moderate'))

  
    if score == 4:
        feedback.append(('✅ Your password is strong! Great job!', 'strong'))
    elif score == 3:
        feedback.append(('⚠️ Your password is moderately strong. Consider improving it.', 'moderate'))
    else:
        feedback.append(('❌ Your password is weak. Please make it stronger.', 'weak'))
    
    # Display feedback
    st.markdown('## 💡 Suggestions to Improve')
    for tip, level in feedback:
        st.markdown(f'<div class="feedback {level}">{tip}</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="info">🔍 Please enter a password to check its strength.</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)