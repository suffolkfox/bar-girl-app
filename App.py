import streamlit as st

# --- 1. CONFIG & THEME ---
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
    /* Secondary button style for Extraction */
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

# Gear Unlock Logic
gear_list = ["Basic Shaker", "AR Recon Goggles", "Tactical Vest", "Signal Flare", "Ignition Fluid"]
current_gear = gear_list[min(st.session_state.level - 1, len(gear_list)-1)]
st.sidebar.info(f"EQUIPPED: {current_gear}")

# --- 4. MAIN INTERFACE ---
st.title("🍸 BAR GIRL")

# IMAGE SECTION
# This uses the image file name you provided earlier
try:
    st.image("1769968494770.png", use_container_width=True)
except:
    st.image("1000072025.jpg", use_container_width=True)

st.write(f"💬 *'Grid calibrated. Based on Angela's intel, we're ready to deploy.'*")

# --- 5. SEARCH LOGIC ---
mode = st.radio("MISSION TYPE:", ["Local Recon (Near Me)", "Scout Ahead (New City)"])

target_city = ""
if mode == "Scout Ahead (New City)":
    target_city = st.text_input("ENTER TARGET CITY:", placeholder="e.g. Peterborough, London...")

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
        
        st.success(f"Target Acquired! +25 XP")
        st.markdown(f"### [📍 OPEN COORDINATES]({maps_url})")
    else:
        st.error("Select a vibe first, soldier!")

# --- 6. EMERGENCY EXTRACTION ---
st.markdown("---")
st.subheader("🚨 EMERGENCY PROTOCOLS")
st.write("Extraction required? Send the signal.")

if st.button("REQUEST EXTRACTION"):
    st.error("📡 DISTRESS SIGNAL SENT... TRACING GPS.")
    uber_url = "https://m.uber.com/ul/?action=setPickup&pickup=my_location"
    
    st.markdown(f"### [🛸 CLICK HERE FOR UBER]({uber_url})")
    st.write("📞 **Local HQ:** 01733 123456 (Peterborough Cars)")
    st.info("Bar Girl: 'Sit tight. I've flagged your location.'")

st.caption("Bar Girl Global Tactical Ops © 2026")
