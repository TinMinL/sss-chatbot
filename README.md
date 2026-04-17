# AI Chatbot for Secondary School Students (Demo)

## Project Overview
This repository contains the prototype/demo of the generative AI-powered chatbot developed for secondary school students in Hong Kong. 

This project was developed as part of the **COMP 3510SEF / COMP S351F - Software Project Management** course. Please note that per course guidelines, the emphasis of this project is on the application of project management methodologies (Agile/Scrum, EVM, Risk Management) rather than full-scale commercial software development.

## Team Members
* **Project Manager:** Chan Hiu Chun (14238060)
* **Business Analyst / UI/UX:** Hung Wing Yan (14012359)
* **Backend Developer:** To Lok Yin (14218233)
* **Frontend Developer:** Lam Ka Ho (14096514)
* **Database Admin:** Kwan Ka Shing (14112125)
* **QA Tester:** Tam Chi Tin (14099682)
* **Prompt Engineer:** Chan Wai Nok (14063175)
* **Doc Controller / Release Mgr:** Fok Ho Fai (13187776)

## System Architecture & Tech Stack
* **Frontend (Presentation Layer):** Lightweight Vanilla HTML/CSS/JS (optimized for fast loading times).
* **Backend (Application Layer):** Python (Flask API Gateway & Logic).
* **Database (Data Layer):** SQLite (Session Logs & User Auth).
* **AI Engine (Knowledge Layer):** DeepSeek LLM API with Retrieval-Augmented Generation (RAG) constraints to ensure Zero Hallucination and curriculum alignment.

## Repository Structure
* `/frontend/` - Contains all HTML, CSS, and JavaScript files for the web-based chat interface.
* `/backend/` - Contains the Python API gateway and logic.

## Prerequisites
To run this demo locally, you will need:
* Python 3.8 or higher
* A valid DeepSeek API Key (You can get one for free at platform.deepseek.com)

## 🚀 How to Run the Application (One-Click Setup)

We have implemented an automated deployment script for seamless User Acceptance Testing (UAT).

**1. Clone the repository:**
```bash
git clone [https://github.com/TinMinL/sss-chatbot.git](https://github.com/TinMinL/sss-chatbot.git)
cd sss-chatbot
```

**2. Run the Launcher:**
Simply double-click the `start.bat` file in the root directory. 

**3. API Key Configuration:**
* If this is your first time running the application, the terminal will safely prompt you to paste your **DeepSeek API Key**.
* The script will automatically generate a secure `.env` file for you and install all required Python dependencies.
* The frontend UI will automatically open in your default browser at `http://localhost:8000`.

## ⚠️ Important Notes for Assessment
* **Cost Management Constraints:** To adhere to our Earned Value Management (EVM) cost baselines (CPI tracking), the API calls in this demo are restricted by token limits per user session. 
* **Quality Assurance (QA) & Security:** Hardcoding API keys is strictly prohibited in our repository. The auto-prompt feature in our deployment script ensures secure environment variable management. As documented in the project report, rigorous AI Safety Testing has been conducted to strictly mitigate hallucination risks.
