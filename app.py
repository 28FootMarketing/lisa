import streamlit as st

st.set_page_config(page_title="Lisa - Parent Connector", page_icon="🤝", layout="centered")

st.title("🤝 Lisa: The Connector")
st.subheader("Parent Communication & Retention")

st.markdown("**Style of Play:** Smart, communicative, and relationship-driven")

st.markdown("""
Lisa bridges the gap between parents and the recruiting process.  
She answers common concerns, helps clarify next steps, and ensures families stay engaged.

> “Lisa brings calm to the chaos, translating the recruiting grind into confident, informed decisions.”
""")

st.header("Step 1: Who Are You Supporting?")
relation = st.selectbox("Select your role:", ["Parent", "Guardian", "Mentor", "Relative"])
athlete_grade = st.selectbox("Student-Athlete's Current Grade:", ["9th", "10th", "11th", "12th", "Gap Year"])
sport = st.text_input("Sport Played by Student-Athlete:")

st.header("Step 2: Top Questions on Your Mind")
concerns = st.multiselect("What are your biggest questions right now?", [
    "How do I help my child get recruited?",
    "What should we be doing each year of high school?",
    "How do we contact coaches?",
    "What should go in a recruiting video?",
    "How do I stay involved without overstepping?",
    "How do I keep my child motivated?",
    "How much does this process usually cost?",
    "What if my child is not a starter?",
    "What role do grades and test scores play?"
])

st.header("Step 3: Support Options")
interest = st.radio("Would you like:", [
    "Personalized roadmap for your family",
    "Weekly updates on what to do next",
    "Answers to my specific questions",
    "Help staying organized throughout this process"
])

contact_method = st.selectbox("Preferred method of communication:", ["Email", "Text Message", "Both"])
contact_info = st.text_input("Your Contact Info:")

if st.button("Get Lisa’s Guidance"):
    st.success("✅ Lisa has prepared personalized guidance for your family.")
    st.markdown(f"""
    **Role:** {relation}  
    **Athlete Grade:** {athlete_grade}  
    **Sport:** {sport}  
    **Top Concerns:** {', '.join(concerns)}  
    **Support Interest:** {interest}  
    **Contact:** via {contact_method} → {contact_info}
    """)
    st.info("Lisa says: We do this together. One step, one decision, one opportunity at a time.")
    st.balloons()
def run():
    # Move your entire app logic into this function.
    st.title("Agent Name")
    # ... rest of the agent's interface ...
