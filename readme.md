# Cold Email Generator

An AI-powered application that automates personalized business outreach by generating tailored cold emails from job postings. The tool analyzes hiring requirements, matches them with relevant portfolio projects, and creates customized outreach emails using Large Language Models (LLMs).

## Overview

The application streamlines the process of identifying potential client needs and crafting relevant outreach messages. Given a job posting URL, it:

* Extracts and analyzes job requirements from career pages
* Identifies key technical skills and hiring needs
* Matches requirements against an internal project portfolio
* Generates personalized cold emails with relevant case studies

## Architecture

```text
Job Posting URL
       │
       ▼
Web Scraping
       │
       ▼
Skill & Requirement Extraction
       │
       ▼
Portfolio Similarity Search
       │
       ▼
Relevant Project Retrieval
       │
       ▼
AI-Powered Email Generation
```

## Technology Stack

* **LLM:** Llama 3.1 (70B) via Groq
* **Framework:** LangChain
* **Vector Database:** ChromaDB
* **Frontend:** Streamlit
* **Data Processing:** Pandas
* **Web Scraping:** LangChain WebBaseLoader

## Project Structure

```text
cold-email-generator/
│
├── app/
│   ├── resource/
│   │   └── my_portfolio.csv
│   ├── chains.py
│   ├── portfolio.py
│   ├── utils.py
│   └── main.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### Clone Repository

```bash
git clone https://github.com/<your-username>/ColdEmailGeneratorTool.git
cd ColdEmailGeneratorTool
```

### Create Virtual Environment

```bash
python -m venv .venv
```

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

> Ensure the `.env` file is excluded from version control.

## Run the Application

```bash
streamlit run app/main.py
```

The application will be available at:

```text
http://localhost:8501
```

## Usage

1. Launch the application.
2. Enter a job posting URL.
3. Generate a personalized outreach email.
4. Review the extracted requirements and matched portfolio references.

## Key Features

* Automated job description analysis
* Structured skill extraction using LLMs
* Semantic portfolio matching with ChromaDB
* Context-aware cold email generation
* Interactive Streamlit interface

## License

This project was developed as a demonstration of Generative AI, LangChain, and Retrieval-Augmented Generation (RAG) concepts and is intended for educational and portfolio purposes.
