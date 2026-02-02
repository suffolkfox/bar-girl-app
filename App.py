import streamlit as st

# --- 1. CONFIG & THEME ---
st.set_page_config(page_title="Bar Girl App", page_icon="🍸", layout="centered")

# Custom Cyberpunk Styling
st.markdown("""
    <style>
    .main { background-color: #1a1a2e; color: #f0f0f0; }
    .stButton>button {
        background: linear-gradient(45deg, #ff416c, #ff4b2b);
        color: white; border-radius: 12px; border: none;
        height: 3.5em; width: 100%; font-weight: bold; font-size: 1.2em;
    }
    /* Emergency Extraction Button Style */
    div.stButton > button:first-child[data-testid="baseButton-secondary"] {
        background: linear-gradient(45deg, #111, #444);
        border: 2px solid #ff4b2b;
    }
    .stSelectbox label, .stRadio label { color: #ff4b2b !important; font-weight: bold; }
    h1 { text-align: center; color: #ff4b2b; text-shadow: 2px 2px #000; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SESSION STATE (XP & PROGRESS) ---
if 'xp' not in st.session_state: st.session_state.xp = 0
if 'level' not in st.session_state: st.session_state.level = 1

def gain_xp():
    st.session_state.xp += 25
    if st.session_state.xp >= 100:
        st.session_state.level += 1
        st.session_state.xp = 0
        st.balloons()

# --- 3. SIDEBAR HUD ---
st.sidebar.title("🪖 TACTICAL HUD")
st.sidebar.subheader(f"RANK: LEVEL {st.session_state.level}")
st.sidebar.progress(st.session_state.xp / 100)

st.sidebar.markdown("---")
st.sidebar.write("🏆 **LEADERBOARD**")
st.sidebar.write(f"1. **SuffolkFox** (Level {st.session_state.level})")
st.sidebar.write("2. **Angela** (Level 1)")

gear = "Basic Shaker"
if st.session_state.level >= 2: gear = "AR Recon Goggles"
if st.session_state.level >= 5: gear = "Ignition Fluid"
st.sidebar.info(f"EQU
