import os, io, requests, pdfplumber, re
import streamlit as st
from PIL import Image
import pytesseract

# ========= PUT YOUR KEYS HERE ==========
GEMINI_KEY = "you_gemini_api"
TAVILY_KEY = "your_tavily_api"
# =======================================


# ================= PAGE CONFIG ==================
st.set_page_config(
    page_title="Ultra Research AI",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ================== PREMIUM UI CSS ===================
st.markdown("""
<style>

/* Import clean modern font */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* Global reset */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
    background: #F1F5F9 !important;
}

/* Remove Streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/********** HERO SECTION **********/
.hero-bg {
    padding: 3rem 1rem;
    text-align: center;
    background: linear-gradient(90deg, #2563EB 0%, #1D4ED8 100%);
    border-radius: 0px 0px 18px 18px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.1);
    margin-bottom: 2rem;
}

.hero-title {
    font-size: 3rem;
    font-weight: 800;
    color: white;
    margin-bottom: 0.4rem;
    width : 100%;
}

.hero-sub {
    color: #E2E8F0;
    font-size: 1.2rem;
}


/********** GLASS INPUT CARD **********/
.glass-card {
    background: white;
    padding: 2rem 2.5rem;
    border-radius: 18px;
    max-width: 1100px;
    margin: auto;
    box-shadow: 0 4px 25px rgba(0,0,0,0.08);
    border: 1px solid #E2E8F0;
}


/********** FORM ELEMENT STYLING **********/
.stTextInput > div > div > input,
.stTextArea textarea {
    border-radius: 10px !important;
    border: 2px solid #CBD5E1 !important;
    padding: 14px !important;
    transition: 0.3s ease !important;
    background: #FFFFFF !important;
    font-size: 15px !important;
}

.stTextInput > div > div > input:focus,
.stTextArea textarea:focus {
    border-color: #2563EB !important;
    box-shadow: 0 0 0 3px rgba(37,99,235,0.3) !important;
}


/********** FILE UPLOADER **********/
.stFileUploader {
    border: 2px dashed #CBD5E1 !important;
    background: #FAFAFA !important;
    border-radius: 12px !important;
    padding: 1.5rem !important;
}

.stFileUploader:hover {
    border-color: #2563EB !important;
    background: #EFF6FF !important;
}


/********** CHECKBOX **********/
.stCheckbox {
    background: white;
    padding: 10px;
    border-radius: 10px;
    border: 1px solid #E2E8F0;
}


/********** BUTTON STYLE (BLUE to ORANGE) **********/
.stButton > button {
    background: linear-gradient(90deg, #2563EB, #F97316) !important;
    color: white !important;
    padding: 14px 28px !important;
    border-radius: 10px !important;
    border: none !important;
    font-size: 17px !important;
    font-weight: 600 !important;
    margin-top: 1rem !important;
    transition: 0.25s ease;
}
.stButton > button:hover {
    background: linear-gradient(90deg, #1D4ED8, #EA580C) !important;
    transform: translateY(-2px);
}



/********** REPORT CARD **********/
.report-card {
    background: white;
    padding: 3rem;
    border-radius: 20px;
    max-width: 1100px;
    margin: 2rem auto;
    border: 1px solid #E2E8F0;
    box-shadow: 0 8px 35px rgba(0,0,0,0.07);
}

/********** HEADINGS **********/
.report-card h1 {
    color: #1E293B;
    font-weight: 800;
    font-size: 2.2rem;
    border-left: 6px solid #F97316;
    padding-left: 14px;
}

.report-card h2 {
    color: #334155;
    font-weight: 700;
    font-size: 1.6rem;
    border-left: 4px solid #2563EB;
    padding-left: 12px;
    margin-top: 2rem;
}

.report-card h3 {
    color: #475569;
    font-weight: 600;
    font-size: 1.25rem;
    margin-top: 1.5rem;
}

.report-card p, .report-card li {
    color: #475569;
    font-size: 16px;
    line-height: 1.75;
}


/********** LINKS **********/
.report-card a {
    color: #2563EB !important;
    font-weight: 600;
}
.report-card a:hover {
    color: #F97316 !important;
}

/********** FOOTER **********/
.footer {
    text-align: center;
    margin-top: 3rem;
    color: #64748B;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)



# ================= INPUT HELPERS ===================
def extract_text_image(file):
    img = Image.open(file)
    return pytesseract.image_to_string(img)

def extract_text_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for p in pdf.pages:
            t = p.extract_text()
            if t:
                text += t + "\n"
    return text

def tavily_search(query):
    if not TAVILY_KEY:
        return []
    try:
        r = requests.post("https://api.tavily.com/search", json={"query":query, "api_key":TAVILY_KEY})
        return r.json().get("results", [])
    except:
        return []

def gemini_generate(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_KEY}"
    r = requests.post(url, json={"contents":[{"parts":[{"text":prompt}]}]})
    if r.status_code != 200:
        return "ERROR: " + r.text
    data = r.json()
    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except:
        return str(data)


# ================= HERO =====================
st.markdown("""
<div class="hero-bg">
    <div class="hero-title">🔍 Ultra Research AI</div>
    <div class="hero-sub">Professional & Educational research reports</div>
</div>
""", unsafe_allow_html=True)


# ================= INPUT CARD =====================
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

query = st.text_input("Research Query", placeholder="Enter your research topic...")
evidence_block = st.text_area("Additional Evidence (optional)", height=120)

uploaded = st.file_uploader("Upload PDF / TXT / PNG / JPG", type=["pdf","txt","png","jpg","jpeg"])
web_search = st.checkbox("Enable Tavily Web Search", value=False)

if st.button("Generate Research Report 🚀"):
    st.info("Processing...")

    evidence = []

    if evidence_block.strip():
        evidence.append({"title":"User Evidence","text":evidence_block})

    if uploaded:
        if uploaded.name.endswith(".pdf"):
            text = extract_text_pdf(uploaded)
        elif uploaded.name.endswith(".txt"):
            text = uploaded.read().decode("utf-8")
        else:
            text = extract_text_image(uploaded)
        evidence.append({"title":uploaded.name,"text":text})

    if web_search:
        for r in tavily_search(query):
            evidence.append({"title":r.get("title","Web"), "text":r.get("snippet",""), "url":r.get("url","")})

    evtext = ""
    for i, ev in enumerate(evidence):
        evtext += f"\nE{i+1}: {ev['title']}\n{ev['text']}\n"


    prompt = f"""
Write a professional research report in Markdown.

Query: {query}

Evidence:
{evtext}

Follow EXACT structure:

# Research Report: {query}
## Executive Summary
## Key Findings
## Evidence At-a-Glance
## Deep Analysis
### Background & Context
### Technical Opportunities
### Practical Applications
### Risks, Limitations & Safety
### Implementation Considerations
## Recommendations
## Research Gaps
## Conclusion
## References
"""

    result = gemini_generate(prompt)

    st.markdown("</div>", unsafe_allow_html=True)

    # Display Report
    st.markdown('<div class="report-card">', unsafe_allow_html=True)
    st.markdown(result, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


st.markdown('<div class="footer">© Ultra Research AI — Powered by Ashok - ashokkumarboya93@gmail.com</div>',
            unsafe_allow_html=True)

