Cold Email Generator Tool
The Cold Email Generator is an end-to-end Generative AI application built to help software and AI service companies streamline their business development outreach. By providing a URL to a client's career page, the tool leverages a Large Language Model (LLM) to scrape the web page, extract the core technical requirements, dynamically match those skills against the company's internal project portfolio database, and compose a highly personalized cold email with relevant case study links.

🏗️ Architecture Overview
The application processes information dynamically through the following pipeline:

Web Scraping: LangChain's WebBaseLoader extracts raw HTML and text content from a target company's job posting URL.

Entity Extraction: An LLM structures the messy raw job description into a clean JSON format highlighting the specific required roles and technical skills.

Semantic Portfolio Retrieval: The extracted technical skills are used as semantic queries against an internal portfolio database stored in ChromaDB. It retrieves specific case studies matching the desired tech stack.

Email Synthesis: The LLM integrates the job details with the retrieved portfolio links using tailored prompt templates to draft a polished, professional business outreach message.

🛠️ Tech Stack & Key Technologies
Orchestration Framework: LangChain (Prompts, Chains, Document Loaders)

Large Language Model: Llama 3.1 (70 Billion Parameter model)

Inference Platform: Groq Cloud (Leveraging Fast LPUs)

Vector Database: ChromaDB (Persistent storage configuration)

User Interface: Streamlit (For a lightweight, reactive web app interface)

Data Handling: Pandas (To ingest underlying CSV project portfolios)

📁 Project Structure
Plaintext
cold-email-generator/
│
├── app/
│   ├── resources/
│   │   └── my_portfolio.csv      # Company tech stacks and corresponding case study links
│   ├── chains.py                 # LLM configurations, prompt templates, and LangChain wrappers
│   ├── main.py                   # Streamlit application orchestration logic
│   ├── portfolio.py              # ChromaDB client initialization and query routing logic
│   └── utils.py                  # Text processing, cleaning, and preprocessing utilities
│
├── .env                          # Local environment variables configuration file (Ignored in Git)
├── requirements.txt              # Application Python package dependencies
└── README.md                     # Project documentation overview
⚙️ Installation & Setup
Follow these steps to set up the repository locally:

1. Clone the Repository
Bash
git clone https://github.com/codebasics/project-cold-email-generator.git
cd project-cold-email-generator
2. Install Dependencies
Ensure you have Python installed, then run:

Bash
pip install -r requirements.txt
3. Setup Your Environment Variables
Create a .env file in your root folder directory and append your specific Groq API Key:

Plaintext
GROQ_API_KEY=your_actual_groq_api_key_here
⚠️ Note: Make sure you obtain your key via the official Groq Console and never commit this .env file to public version control repositories.

🚀 Running the Application
Launch the Streamlit web server locally using the terminal command:

Bash
streamlit run app/main.py
Once running, navigate to the local network port provided in your console (usually http://localhost:8501). Enter any active hiring career page link (such as a software engineer requirement on a public job board) to generate your customized pitch emails immediately.