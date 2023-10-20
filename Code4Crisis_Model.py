import streamlit as st

st.set_page_config(
    page_title="C4C Model",
    page_icon="🤖",
)

st.header("Code4Crisis ⚔️", divider='red')
st.sidebar.markdown("# Use Model 🤖")

choice = st.selectbox("Pick a sample input", ["Sample 1", "Sample 2", "Sample 3"])

if choice == "Sample 1":
    st.text('''Topic: UAE-Iran islands dispute complicates regional diplomacy.
Country 1: Iran 
Country 2: UAE
Region: Abu Musa''')
    choice = 1
elif choice == "Sample 2":
    st.text('''Topic: Coordinating international responses to Ethiopia-Sudan tensions.
Country 1: Ethiopia
Country 2: Sudan
Region: Al-Fashqa''')
    choice = 2
elif choice == "Sample 3":
    st.text('''Topic: Azerbaijan-Armenia conflict over Nagorno-Karabakh region leads to civilian casualties.
Country 1: Armenia
Country 2: Azerbaijan
Region: Nagorno-Karabakh''')
    choice = 3

if st.button("Run Model", type="primary"):
    if choice == 3:
        st.error("Crisis may have started or is about to start.")
    else:
        st.success("A crisis have not been detected.")

st.divider()
st.caption("Made by code4crisis")
