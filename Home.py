import streamlit as st
import pandas as p
from pathlib import Path
import base64

def project_card(title, image, description, url):
    st.html(
        f"""
        <style>
        .project-card {{
            transition: transform 0.3s ease-in-out;
        }}
        .project-card:hover {{
            transform: scale(1.05);
        }}
        </style>
        <div class="project-card" style="border-radius: 15px; padding: 15px; background-color: white; box-shadow: 2px 2px 10px #aaa; margin-bottom: 20px ">
            <h4 style="color: #333;">{title}</h4>
            <img src="https://raw.githubusercontent.com/Merthadam/portfolio/main/static/images/{image}" style="width:100%; border-radius:10px;">
            <p>{description}</p>
            <a href="{url}" target="_blank" style="text-decoration: none;">
                <button style="background-color: #007BFF; color: white; padding: 10px; border: none; border-radius: 5px; cursor: pointer;">
                    See Code
                </button>
            </a>
        </div>
        """
    )

# ---------------------------
# Page & CSS
# ---------------------------
st.set_page_config(layout="wide", page_title="Adam • Portfolio", page_icon="🎯")
st.markdown(
    """
    <style>
      .block-container { padding-top: 2rem; padding-bottom: 3rem; }
      .avatar {
        width: 180px; height: 180px; object-fit: cover;
        border-radius: 50%;
        box-shadow: 0 10px 24px rgba(0,0,0,.25);
        border: 3px solid rgba(255,255,255,.1);
      }
      /* prettier pill links */
      .pill {
        display:inline-block; padding:.5rem .9rem; margin-right:.5rem; margin-bottom:.5rem;
        border-radius:999px; font-weight:600; text-decoration:none; font-size:.92rem;
        background: linear-gradient(135deg,#22c55e,#84cc16);
        color:#0f172a; border:1px solid rgba(255,255,255,.12);
        box-shadow:0 8px 24px rgba(34,197,94,.25);
        transition: transform .15s ease, filter .15s ease;
      }
      .pill:hover { filter:brightness(.95); transform: translateY(-1px); }
      .muted { color: rgba(255,255,255,0.75); }
      .meta { color: rgba(255,255,255,0.6); font-size:.9rem; }
      /* default links elsewhere (if any) */
      a:not(.pill) { color:#60a5fa; }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# Header
# ---------------------------
st.title("Home")

header_left, header_right = st.columns([1, 2], gap="large")

def embed_avatar(path_str: str):
    path = Path(path_str)
    if path.exists():
        b64 = base64.b64encode(path.read_bytes()).decode()
        st.markdown(f'<img src="data:image/jpeg;base64,{b64}" alt="Profile" class="avatar">', unsafe_allow_html=True)
    else:
        st.warning(f"Profile image not found at `{path}`")

with header_left:
    embed_avatar("static/images/profile_pic.jpg")

with header_right:
    st.markdown("### Hi, I’m Adam")
    st.markdown(
        "I’m a university student at **ELTE** (Budapest). This page showcases "
        "a selection of my projects across **full-stack web** and **data apps**."
    )
    st.markdown(
        "- Focus: showcasing my skillset through a portfolio page that shows some of my work.\n"
        "- Tools I used: **Laravel**, **React**, **Vite**, **Tailwind**, **Streamlit**, **Pandas**, **Java** **lib_gdx** and many other tools.\n"
    )
    st.markdown(
        """
        <div>
          <a class="pill" href="https://github.com/Merthadam" target="_blank">GitHub</a>
          <a class="pill" href="www.linkedin.com/in/ádám-mérth-93a582377" target="_blank">LinkedIn</a>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown('<span class="meta">Budapest · Open to internships & junior roles</span>', unsafe_allow_html=True)

st.divider()

# ---------------------------
# Intro (non-project text)
# ---------------------------
st.subheader("Selected Projects")
st.markdown(
    "Below is a curated list of my recent work. Each card links to the source code. "
    "I focus on readable code, predictable state management, and clear UX."
)

# ---------------------------
# Project grid (unchanged)
# ---------------------------
col3, col4 = st.columns(2, gap="medium")
df = p.read_csv("data.csv", sep=";")

with col3:
    for _, row in df[: len(df) // 2].iterrows():
        project_card(row["title"], row["image"], row["description"], row["url"])

with col4:
    for _, row in df[len(df) // 2 :].iterrows():
        project_card(row["title"], row["image"], row["description"], row["url"])
        
