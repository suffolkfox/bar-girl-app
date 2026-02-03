import streamlit as st

# --- 1. CONFIG & STYLING ---
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

# --- 2. SESSION STATE ---
if 'xp' not in st.session_state: st.session_state.xp = 0
if 'level' not in st.session_state: st.session_state.level = 1
if 'vibe_choice' not in st.session_state: st.session_state.vibe_choice = "-- Select --"

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
st.sidebar.write(f"1. **SuffolkFox** (Lvl {st.session_state.level})")
st.sidebar.write("2. **Angela** (Lvl 1)")

# --- 4. DYNAMIC VISUALS ---
st.title("🍸 BAR GIRL")

if st.session_state.level >= 10:
    img_file, caption_text = "victory.png", "TACTICAL LEGEND: Level 10 Achieved!"
elif st.session_state.vibe_choice == "A Nice Beer 🍺":
    img_file, caption_text = "beer_review.png", "Analyzing hop profiles..."
else:
    img_file, caption_text = "1769968494770.png", "Bar Girl: 'Ready for deployment.'"

try:
    st.image(img_file, caption=caption_text, use_container_width=True)
except:
    st.error(f"⚠️ Deployment Error: Ensure '{img_file}' is on GitHub.")

# --- 5. SEARCH & SCOUT LOGIC ---
mode = st.radio("MISSION TYPE:", ["Local Recon (Near Me)", "Scout Ahead (New City)"])

target_city = ""
if mode == "Scout Ahead (New City)":
    target_city = st.text_input("ENTER TARGET CITY:", placeholder="e.g. London, Tokyo, Peterborough...")

st.session_state.vibe_choice = st.selectbox("CHOOSE YOUR VIBE:", ["-- Select --", "A Nice Beer 🍺", "Fancy Cocktails 🍹", "Good Pub Food 🍔"])

# Search Function
def run_tactical_scan():
    if st.session_state.vibe_choice != "-- Select --":
        gain_xp()
        keywords = {"A Nice Beer 🍺": "craft+beer+pub", "Fancy Cocktails 🍹": "cocktail+bar", "Good Pub Food 🍔": "gastropub+food"}
        query = keywords[st.session_state.vibe_choice]
        
        location = f"in+{target_city.replace(' ', '+')}" if target_city else "near+me"
        maps_url = f"https://www.google.com/maps/search/{query}+{location}"
        
        st.success(f"Target Acquired! +25 XP")
        st.markdown(f"### [📍 OPEN COORDINATES]({maps_url})")
    else:
        st.error("Select a vibe first!")

# PINT REVIEW UI
if st.session_state.vibe_choice == "A Nice Beer 🍺":
    st.markdown("### 📋 TACTICAL PINT LOG")
    st.text_area("Observations:", placeholder="How's the brew?")
    st.slider("Rating:", 1.0, 5.0, 4.5)
    if st.button("LOG MISSION & RUN SCAN"):
        run_tactical_scan()
else:
    if st.button("RUN SCAN"):
        run_tactical_scan()

# --- 6. EXTRACTION ---
st.markdown("---")
if st.button("🚨 REQUEST EXTRACTION"):
    st.error("📡 DISTRESS SIGNAL SENT...")
    st.markdown("### [🛸 CLICK FOR UBER](https://m.uber.com/ul/?action=setPickup&pickup=my_location)")
