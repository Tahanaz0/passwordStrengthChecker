import streamlit as st
import re

# Page configuration
st.set_page_config(page_title='Password Strength Checker', page_icon='🔒', layout='centered')

# Custom Styling
st.markdown(
    """
    <style>
        body { background-color: #f4f4f4; font-family: Arial, sans-serif; }
        .main { background: white; padding: 2rem; border-radius: 10px; box-shadow: 0px 4px 12px rgba(0,0,0,0.1); }
        h1 { color: #333; text-align: center; }
        .feedback { font-size: 16px; padding: 10px; border-radius: 5px; margin: 5px 0; }
        .strong { background-color: #d4edda; color: #155724; }
        .moderate { background-color: #fff3cd; color: #856404; }
        .weak { background-color: #f8d7da; color: #721c24; }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown('<div class="main">', unsafe_allow_html=True)
st.title('🔒 Password Strength Checker')
st.markdown("## Enter your password to check its strength 🛡️")

# Input field
password = st.text_input('Enter your password', type='password')
feedback = []
score = 0

if password:
    if len(password) < 8:
        feedback.append(('❌ Length should be at least 8 characters', 'weak'))
    else:
        score += 1

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append(('❌ Password should contain at least one uppercase and one lowercase letter', 'weak'))

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append(('❌ Password should contain at least one digit', 'moderate'))

    if re.search(r'[@#$&]', password):
        score += 1
    else:
        feedback.append(('❌ Password should contain at least one special character (@#$&)', 'moderate'))

    # Password strength message
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
    st.info('🔍 Please enter a password to check its strength.')

st.markdown('</div>', unsafe_allow_html=True)
