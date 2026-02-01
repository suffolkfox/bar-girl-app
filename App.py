import streamlit as st

# --- CONFIG & STYLES ---
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
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE (XP & LEVELS) ---
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

gear = "Basic Shaker"
if st.session_state.level >= 2: gear = "AR Recon Goggles"
if st.session_state.level >= 3: gear = "Ignition Fluid"
st.sidebar.info(f"EQUIPPED: {gear}")

# --- MAIN INTERFACE ---
st.title("🍸 BAR GIRL")
st.write(f"💬 *'Current rank: {st.session_state.level}. Ready for the next mission?'*")

mode = st.radio("MISSION TYPE:", ["Local Recon (Near Me)", "Scout Ahead (New City)"])

target_city = ""
if mode == "Scout Ahead (New City)":
    target_city = st.text_input("ENTER TARGET CITY:", placeholder="e.g. London, Paris...")

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
        
        st.success(f"Target Locked! +25 XP")
        st.markdown(f"### [📍 OPEN COORDINATES]({maps_url})")
    else:
        st.error("Select a vibe first, soldier!")
# Add this right under st.title("🍸 BAR GIRL")
st.image("https://raw.githubusercontent.com/suffolkfox/Bar-Girl/main/bargirl_image.jpg")
