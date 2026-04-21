import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load env
load_dotenv()

# Initialize client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Page config
st.set_page_config(page_title="Insurance System", page_icon="💬")

st.title("💬 Insurance Assistant latest")
st.write("Ask anything about insurance policies, claims, coverage, etc.")
st.write("this is new version!")

st.divider()

# ---------------------------
# Feature C: Response Tone
# ---------------------------
tone = st.selectbox(
    "Response Style",
    ["Simple", "Detailed", "Professional"]
)

st.divider()

# ---------------------------
# Feature B: Predefined Questions
# ---------------------------
st.write("💡 Try these:")
col1, col2 = st.columns(2)

preset_query = None

if col1.button("What is term insurance?"):
    preset_query = "What is term insurance?"

if col2.button("How to claim insurance?"):
    preset_query = "How to claim insurance?"

st.divider()

# ---------------------------
# User Input
# ---------------------------
user_query = st.text_area("Enter your query:")

# Override if preset clicked
if preset_query:
    user_query = preset_query

# ---------------------------
# Get Answer
# ---------------------------
if st.button("Get Answer"):
    if user_query.strip() == "":
        st.warning("Please enter a query")
    elif len(user_query.strip()) < 5:
        st.warning("Query too short")
    else:
        with st.spinner("Thinking..."):
            try:
                # System prompt with tone
                system_prompt = f"""
                You are an insurance expert.
                Respond in a {tone.lower()} way.
                Give clear and helpful answers.
                """

                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_query}
                    ]
                )

                answer = response.choices[0].message.content

                st.success("Response:")
                st.write(answer)

                # ---------------------------
                # Feature E: Download Button
                # ---------------------------
                st.download_button(
                    "⬇ Download Answer",
                    answer,
                    file_name="insurance_answer.txt"
                )

            except Exception as e:
                st.error(f"Error: {str(e)}")