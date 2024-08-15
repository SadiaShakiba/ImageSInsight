import streamlit as st

st.html("""
  <style>
    [alt=Logo] {
      height: 3rem;
    }
  </style>
        """)
# --- PAGE SETUP ---
about_page = st.Page(
    "views/about.py",
    title="About",
    icon=":material/home:",
    default=True,
)
plant_page = st.Page(
    "views/Plantdisease.py",
    title="Plant Disease Prediction",
    icon=":material/psychiatry:",
)
project_1_page = st.Page(
    "views/Fracture.py",
    title="Fracture Classification",
    icon=":material/personal_injury:",
)
project_2_page = st.Page(
    "views/polyp.py",
    title="Polyp Segmentation",
    icon=":material/admin_meds:",
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [plant_page,project_1_page, project_2_page],
    }
)


# --- SHARED ON ALL PAGES ---
st.logo("assests\ImageSInsight_2.png")
st.sidebar.markdown("Copyright © [Sadia Shakiba Bhuiyan](https://www.linkedin.com/in/sadia-shakiba-bhuiyan-0b0a57311)")


# --- RUN NAVIGATION ---
pg.run()