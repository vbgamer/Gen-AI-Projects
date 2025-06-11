import streamlit as st
import openai

# Setup OpenRouter-compatible OpenAI client
client = openai.OpenAI(
     api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

# Streamlit UI
st.set_page_config(page_title="AMIGO - GPT", page_icon="🤖")
st.title("🤖 Ask AMIGO - Your Friendly Free AI Assistant")

# Message history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]

# Chat input
user_input = st.chat_input("Ask anything...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("AMIGO is thinking..."):
        response = client.chat.completions.create(
            model="mistralai/devstral-small:free",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": reply})

# Display messages
for msg in st.session_state.messages[1:]:  # Skip system prompt
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
