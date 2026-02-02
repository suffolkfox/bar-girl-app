import streamlit as st

# --- 1. CONFIG & THEME ---
st.set_page_config(page_title="Bar Girl App", page_icon="🍸", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #1a1a2e; color: #f0f0f0; }
    .stButton>button {
        background: linear-gradient(45deg, #ff416c, #ff4b2b);
        color: white; border-radius: 12px; border: none;
        height: 3.5em; width: 100%; font-weight: bold; font-size: 1.2em;
    }
    div.stButton > button:first-child[data-testid="baseButton-secondary"] {
        background: linear-gradient(45deg, #111, #444);
        border: 2px solid #ff4b2b;
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

# --- 4. MAIN INTERFACE ---
st.title("🍸 BAR GIRL")

# DYNAMIC IMAGE LOGIC
# Make sure to upload your files to GitHub with these EXACT names:
# Main Image: 1000072025.jpg
# Beer Review: 1000074247.png
# Victory: 1000074248.png

if st.session_state.level >= 10:
    st.image("1000074248.png", caption="MISSION ACCOMPLISHED: LEVEL 10 REACHED!", use_container_width=True)
elif st.session_state.vibe_choice == "A Nice Beer 🍺":
    st.image("1000074247.png", caption="Scanning for the perfect pint...", use_container_width=True)
else:
    try:
        st.image("1000072025.jpg", use_container_width=True)
    except:
        st.info("Awaiting Bar Girl Visuals...")

st.write(f"💬 *'Ready for deployment. What's the mission objective?'*")

# --- 5. SEARCH LOGIC ---
mode = st.radio("MISSION TYPE:", ["Local Recon", "Scout Ahead"])
if mode == "Scout Ahead":
    target_city = st.text_input("ENTER TARGET CITY:", placeholder="e.g. Peterborough...")

st.session_state.vibe_choice = st.selectbox("CHOOSE YOUR VIBE:", ["-- Select --", "A Nice Beer 🍺", "Fancy Cocktails 🍹", "Good Pub Food 🍔"])

if st.button("RUN SCAN"):
    if st.session_state.vibe_choice != "-- Select --":
        gain_xp()
        query = st.session_state.vibe_choice.replace(" ", "+")
        maps_url = f"https://www.google.com/maps/search/{query}+near+me"
        st.success("Target Acquired!")
        st.markdown(f"### [📍 OPEN COORDINATES]({maps_url})")
        st.rerun() # This refreshes the image instantly
    else:
        st.error("Select a vibe first!")

# --- 6. EXTRACTION ---
st.markdown("---")
if st.button("REQUEST EXTRACTION"):
    st.error("📡 DISTRESS SIGNAL SENT...")
    st.markdown("### [🛸 CLICK FOR UBER](https://m.uber.com/ul/?action=setPickup&pickup=my_location)")
    st.write("📞 **Local HQ:** 01733 123456")

st.caption("Bar Girl Global Tactical Ops © 2026")
