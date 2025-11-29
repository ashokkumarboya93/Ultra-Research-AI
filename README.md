<div align="center">

# 🔍 Ultra Research AI  
### _AI-Powered Research Report Generator — Built with Gemini 2.0 Flash_

A modern, elegant, and intelligent research automation dashboard that transforms queries, PDFs, text files, and images into **professional, structured research reports** using the power of **Google Gemini**, **Tavily Web Search**, and **OCR**.

---

<img src="https://img.shields.io/badge/Framework-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/Model-Gemini_2.0_Flash-4285F4?style=for-the-badge&logo=google&logoColor=white"/>
<img src="https://img.shields.io/badge/Search-Tavily-0EA5E9?style=for-the-badge&logo=googlechrome&logoColor=white"/>
<img src="https://img.shields.io/badge/OCR-Tesseract-5A8DEE?style=for-the-badge&logo=apache&logoColor=white"/>
<img src="https://img.shields.io/badge/UI-Premium_Blue_+_Orange-1E40AF?style=for-the-badge"/>

</div>

---
**Demo Link:** 🔗 [Access Demo]()


# 🌐 Overview

**Ultra Research AI** is a full-stack research generation engine designed for students, researchers, analysts, and professionals who need **instant, high-quality research reports** with structured sections.

The system intelligently processes:
- **Research queries**
- **User-provided evidence**
- **PDF documents**  
- **Images (OCR extraction)**
- **Text files**
- **Real-time web search**

It outputs a highly polished, academic-style research report using a **beautiful UI built in Streamlit**, with **blue-light + orange premium accents**, clean typography, and fully responsive design.

---

# ✨ Features

### 🔮 **1. AI-Generated Research Reports**
Produces complete multi-section reports:
- Executive Summary  
- Key Findings  
- Evidence Table  
- Background & Context  
- Deep Analysis  
- Practical Applications  
- Risks & Limitations  
- Implementation Considerations  
- Recommendations  
- Research Gaps  
- Conclusion  
- References

---

### 📄 **2. Upload Multiple Evidence Types**
Upload:
- PDF  
- TXT  
- JPG / PNG (OCR via Tesseract)  

All extracted evidence is combined intelligently before synthesis.

---

### 🌐 **3. Web Search Automation (Tavily)**
Optional real-time, AI-augmented web search to strengthen reports with live data and citations.

---

### 🎨 **4. Stunning Modern UI**
- Premium **Blue + Orange Professional Theme**  
- Glassmorphism cards  
- Animated buttons  
- Responsive layout  
- Clean typography (Inter)  
- Desktop + Mobile optimized  
- Professional report UI with sidebar-free design  

---

### 📥 **5. Export to Markdown**
One-click export:  
`research_report.md`

---

---

# 🧰 Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Streamlit + Custom CSS |
| Model | Gemini 2.0 Flash |
| Search | Tavily API |
| OCR | Tesseract |
| File Parsing | pdfplumber, Pillow |
| Deployment | Ngrok / Local |
| Language | Python |

---

# 📦 Installation

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/YOUR-USERNAME/ultra-research-ai.git
cd ultra-research-ai
2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Add API Keys

Edit app.py:

GEMINI_KEY = "your_gemini_key"
TAVILY_KEY = "your_tavily_key"

4️⃣ Run the app
streamlit run app.py

5️⃣ For public URL
ngrok http 8501

🚀 Usage Guide
✔ Step 1: Enter your research query

Example:

A deep research review on sustainable battery technologies for EVs

✔ Step 2: Add evidence (optional)

Paste summaries, ideas, notes.

✔ Step 3: Upload any files

PDF → extracted with pdfplumber

Image → extracted using OCR

TXT → instantly parsed

✔ Step 4: Enable web search (optional)

Uses Tavily to add live results.

✔ Step 5: Click “Generate Research Report 🚀”

A fully formatted research paper is generated.

✔ Step 6: Download as Markdown

Perfect for:

Assignments

Research submissions

Blog posts

Reports

📘 Sample Demo Queries

Use these for showcasing the tool:

“How AI will transform global cybersecurity by 2030.”

“The future of battery recycling technologies for EVs.”

“A deep research analysis on AGI safety frameworks.”

“Economic impact of humanoid robotics in manufacturing.”

“Quantum machine learning: opportunities & limitations.”

🧾 Sample Evidence Block
Recent studies show significant progress in sustainable EV battery chemistries,
including solid-state advancements and improved LFP efficiency. Global recycling
rates are increasing due to hydrometallurgical processes, while lifecycle emissions
remain a challenge in emerging economies.
🧪 Test Cases
Test Case	Description
TC01	Generate report with simple query
TC02	Query + evidence block
TC03	Upload PDF (text extraction)
TC04	Image OCR extraction
TC05	Web search enabled
TC06	Missing query validation
TC07	Markdown export
🏗️ Project Architecture
ultra-research-ai/
│── app.py
│── requirements.txt
│── README.md
│── screenshots/
│── assets/
└── data/

👨‍💻 Author

Ashok
AI/ML Engineer Aspirant • Tech Ethnucient

⭐ Support the Project

If you like this project, give it a ⭐ on GitHub — it motivates development and improvements!
