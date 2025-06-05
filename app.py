import streamlit as st

# Title and subtitle
st.set_page_config(page_title="Agent Lisa – Parent Retention Support", layout="centered")
st.title("👩🏽‍💼 Meet Lisa – Parent Communication & Retention Agent")
st.subheader("Guiding Parents Through the Recruiting Process with Care and Clarity")

# Intro
st.markdown("Lisa is your trusted advisor, helping parents stay informed, supported, and ready to advocate for their student-athletes every step of the way.")

# Lisa's style and quote
st.image("https://example.com/lisa-avatar.png", caption="Agent Lisa: Calm. Compassionate. Clear.", use_column_width=True)
st.markdown("> “Every parent needs a playbook too. I make sure they do not feel left behind.”")

# FAQ Simulation
with st.expander("📝 Common Parent Questions I Help Answer"):
    st.markdown("- How do I know if a coach is really interested?")
    st.markdown("- What should I be doing during junior year?")
    st.markdown("- When should I step in—or step back?")
    st.markdown("- What are red flags with offers?")
    st.markdown("- How can I keep my athlete motivated?")

# CTA
st.success("📅 Want personalized updates for your role in the process? Click below.")
st.button("Join the Parent Support List")

