import streamlit as st

# --- 1. CONFIG & HUD STYLING ---
st.set_page_config(page_title="Bar Girl App", page_icon="🍸", layout="centered")

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

# --- 2. INTELLIGENCE (XP & LEVELS) ---
if 'xp' not in st.session_state: st.session_state.xp = 0
if 'level' not in st.session_state: st.session_state.level = 1
if 'vibe_choice' not in st.session_state: st.session_state.vibe_choice = "-- Select --"

def gain_xp():
    st.session_state.xp += 25
    if st.session_state.xp >= 100:
        st.session_state.level += 1
        st.session_state.xp = 0
        st.balloons()

# --- 3. SIDEBAR RADAR ---
st.sidebar.title("🪖 TACTICAL HUD")
st.sidebar.subheader(f"RANK: LEVEL {st.session_state.level}")
st.sidebar.progress(st.session_state.xp / 100)
st.sidebar.write(f"1. **SuffolkFox** (Level {st.session_state.level})")
st.sidebar.write("2. **Angela** (Level 1)")

# --- 4. DYNAMIC VISUALS SECTION ---
st.title("🍸 BAR GIRL")

# This logic checks your status and displays the correct photo
if st.session_state.level >= 10:
    img_file = "victory.png"
    caption_text = "TACTICAL LEGEND: Level 10 Achieved!"
elif st.session_state.vibe_choice == "A Nice Beer 🍺":
    img_file = "beer_review.png"
    caption_text = "Analyzing hop profiles and brew quality..."
else:
    img_file = "1769968494770.png"
    caption_text = "Bar Girl: 'Awaiting your command, soldier.'"

try:
    st.image(img_file, caption=caption_text, use_container_width=True)
except Exception as e:
    st.error(f"⚠️ Deployment Error: Please ensure '{img_file}' is uploaded to GitHub.")

# --- 5. THE MISSION SELECTOR ---
st.session_state.vibe_choice = st.selectbox("CHOOSE YOUR VIBE:", ["-- Select --", "A Nice Beer 🍺", "Fancy Cocktails 🍹", "Good Pub Food 🍔"])

# Special Pint Review Logic
if st.session_state.vibe_choice == "A Nice Beer 🍺":
    st.markdown("### 📋 TACTICAL PINT LOG")
    notes = st.text_area("Observations (Head, Taste, Coldness):", placeholder="Mission notes...")
    rating = st.slider("Tactical Star Rating:", 1.0, 5.0, 4.5)
    
    if st.button("LOG MISSION & SCOUT NEARBY"):
        gain_xp()
        st.success(f"Log Confirmed! XP awarded. Tracking beer spots...")
        st.markdown(f"### [📍 VIEW MAP](https://www.google.com/maps/search/craft+beer+near+me)")
        # No rerun here to keep the notes visible for a second

elif st.button("RUN SCAN"):
    if st.session_state.vibe_choice != "-- Select --":
        gain_xp()
        query = st.session_state.vibe_choice.replace(" ", "+")
        st.markdown(f"### [📍 OPEN COORDINATES](https://www.google.com/maps/search/{query}+near+me)")
    else:
        st.error("Select a vibe before scanning!")

# --- 6. EMERGENCY EXTRACTION ---
st.markdown("---")
if st.button("🚨 REQUEST EXTRACTION"):
    st.error("📡 DISTRESS SIGNAL SENT... EVAC TEAM NOTIFIED.")
    st.markdown("### [🛸 CLICK FOR UBER](https://m.uber.com/ul/?action=setPickup&pickup=my_location)")
    st.write("📞 **Local Backup:** 01733 123456 (Peterborough Cars)")

st.caption("Bar Girl Global Tactical Ops © 2026")
