# sss-chatbot
# AI Chatbot for Secondary School Students (Demo)

## Project Overview
[cite_start]This repository contains the prototype/demo of the generative AI-powered chatbot developed for secondary school students in Hong Kong[cite: 233, 236]. 

[cite_start]This project was developed as part of the **COMP 3510SEF / COMP S351F - Software Project Management** course at HKMU[cite: 234]. [cite_start]Please note that per course guidelines, the emphasis of this project is on the application of project management methodologies (Agile/Scrum, EVM, Risk Management) rather than full-scale commercial software development[cite: 160, 161, 238, 239].

## Team Members
* [cite_start]**Project Manager:** Chan Hiu Chun (14238060) [cite: 309]
* [cite_start]**Business Analyst / UI/UX:** Hung Wing Yan (14012359) [cite: 309]
* [cite_start]**Backend Developer:** To Lok Yin (14218233) [cite: 309]
* [cite_start]**Frontend Developer:** Lam Ka Ho (14096514) [cite: 309]
* [cite_start]**Database Admin:** Kwan Ka Shing (14112125) [cite: 309]
* [cite_start]**QA Tester:** Tam Chi Tin (14099682) [cite: 309]
* [cite_start]**Prompt Engineer:** Chan Wai Nok (14063175) [cite: 309]
* [cite_start]**Doc Controller / Release Mgr:** Fok Ho Fai (13187776) [cite: 309]

## System Architecture & Tech Stack
* [cite_start]**Frontend (Presentation Layer):** Lightweight Vanilla HTML/CSS/JS (optimized for fast loading times on school tablets)[cite: 322, 434, 437].
* [cite_start]**Backend (Application Layer):** Python (API Gateway & Logic)[cite: 439, 440].
* [cite_start]**Database (Data Layer):** SQL (Session Logs & User Auth)[cite: 441, 442].
* [cite_start]**AI Engine (Knowledge Layer):** LLM API with Retrieval-Augmented Generation (RAG) to ensure Zero Hallucination and curriculum alignment[cite: 286, 292, 443, 444, 445].

## Repository Structure
* `/frontend/` - Contains all HTML, CSS, and JavaScript files for the web-based chat interface.
* `/backend/` - Contains the Python API gateway and prompt engineering logic.
* `/database/` - Contains SQL setup scripts and mock schema.
* `/docs/` - Contains RAG textbook reference samples (dummy data) and system architecture diagrams.

## Prerequisites
To run this demo locally, you will need:
* Python 3.8 or higher
* pip (Python package installer)
* A modern web browser
* *(Optional)* DB Browser for SQLite (if using a local SQLite testing database)

## Installation & Setup Guide

**1. Clone the repository:**
```bash
git clone [Insert Your GitHub Repo URL Here]
cd [Your-Repo-Folder-Name]
