import streamlit as st

# --- CONFIG & STYLES ---
st.set_page_config(page_title="Bar Girl App", page_icon="🍸", layout="centered")

# Cyberpunk / Graphic Novel CSS
st.markdown("""
    <style>
    .main { background-color: #1a1a2e; color: #f0f0f0; }
    .stButton>button {
        background: linear-gradient(45deg, #ff416c, #ff4b2b);
        color: white; border-radius: 12px; border: none;
        height: 3.5em; width: 100%; font-weight: bold; font-size: 1.2em;
    }
    .stSelectbox label, .stRadio label { color: #ff4b2b !important; font-weight: bold; }
    h1 { text-align: center; color: #ff4b2b; text-shadow: 2px 2px #000; }
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE (XP & LEADERBOARD) ---
if 'xp' not in st.session_state: st.session_state.xp = 0
if 'level' not in st.session_state: st.session_state.level = 1

def gain_xp():
    st.session_state.xp += 25
    if st.session_state.xp >= 100:
        st.session_state.level += 1
        st.session_state.xp = 0
        st.balloons()

# --- SIDEBAR HUD ---
st.sidebar.title("🪖 TACTICAL HUD")
st.sidebar.subheader(f"RANK: LEVEL {st.session_state.level}")
st.sidebar.progress(st.session_state.xp / 100)

# Leaderboard Mockup
st.sidebar.markdown("---")
st.sidebar.write("🏆 **LEADERBOARD**")
st.sidebar.write(f"1. **SuffolkFox** (Level {st.session_state.level})")
st.sidebar.write("2. **Angela** (Level 1)")

# Gear Unlock Logic
gear = "Basic Shaker"
if st.session_state.level >= 2: gear = "AR Recon Goggles"
if st.session_state.level >= 5: gear = "Ignition Fluid (Flaming Bottles)"
st.sidebar.info(f"EQUIPPED: {gear}")

# --- MAIN INTERFACE ---
st.title("🍸 BAR GIRL")

# DISPLAY YOUR CHARACTER IMAGE
# This pulls the image from your GitHub folder
try:
    st.image("1769968494770.png", use_container_width=True)
except:
    st.info("Character Image Loading... (Make sure the PNG is uploaded to GitHub!)")

st.write(f"💬 *'Target identified. Let's find you a spot, soldier.'*")

mode = st.radio("MISSION TYPE:", ["Local Recon (Near Me)", "Scout Ahead (New City)"])

target_city = ""
if mode == "Scout Ahead (New City)":
    target_city = st.text_input("ENTER TARGET CITY:", placeholder="e.g. London, Tokyo, Peterborough...")

vibe = st.selectbox("CHOOSE YOUR VIBE:", ["-- Select --", "A Nice Beer 🍺", "Fancy Cocktails 🍹", "Good Pub Food 🍔"])

if st.button("RUN SCAN"):
    if vibe != "-- Select --":
        gain_xp()
        keywords = {
            "A Nice Beer 🍺": "craft+beer+pub",
            "Fancy Cocktails 🍹": "cocktail+bar",
            "Good Pub Food 🍔": "gastropub+food"
        }
        query = keywords[vibe]
        
        if mode == "Scout Ahead (New City)" and target_city:
            final_query = f"{query}+in+{target_city.replace(' ', '+')}"
        else:
            final_query = f"{query}+near+me"
            
        maps_url = f"https://www.google.com/maps/search/{final_query}"
        
        st.success(f"Scanning Complete! +25 XP")
        st.markdown(f"### [📍 OPEN COORDINATES]({maps_url})")
    else:
        st.error("Select a vibe first!")

st.caption("Bar Girl Global Tactical Ops © 2026")
