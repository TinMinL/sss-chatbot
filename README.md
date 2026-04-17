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
* **Backend (Application Layer):** Python (API Gateway & Logic).
* **Database (Data Layer):** SQL (Session Logs & User Auth).
* **AI Engine (Knowledge Layer):** LLM API with Retrieval-Augmented Generation (RAG) to ensure Zero Hallucination and curriculum alignment.

## Repository Structure
* `/frontend/` - Contains all HTML, CSS, and JavaScript files for the web-based chat interface.
* `/backend/` - Contains the Python API gateway and logic.
* `/database/` - Contains SQL setup scripts and mock schema.

## Prerequisites
To run this demo locally, you will need:
* Python 3.8 or higher
* pip (Python package installer)
* A modern web browser

## Installation & Setup Guide

**1. Clone the repository:**
```bash
git clone https://github.com/TinMinL/sss-chatbot.git
cd sss-chatbot
```

**2. Start the Frontend UI:**
Navigate to the `/frontend` folder and use a local server to avoid CORS issues:
```bash
cd frontend
python -m http.server 8000
# Open your browser and go to http://localhost:8000
```

## ⚠️ Important Notes for Assessment
* **Cost Management Constraints:** To adhere to our Earned Value Management (EVM) cost baselines (CPI tracking), the API calls in this demo are restricted by token limits per user session. Frequent queries are cached locally to minimize cloud API costs.
* **Quality Assurance (QA):** As documented in the project report, rigorous automated system testing and AI Safety Testing have been conducted to evaluate prompt retrieval accuracy and strictly mitigate hallucination risks. The setup of these automated tests and performance reporting is an integral part of our QA pipeline.
