AI Marketing Brochure Generator
Project Overview
The AI Marketing Brochure Generator is a Streamlit application designed to automate the initial phase of content creation for marketing brochures. It leverages Large Language Models (LLMs) from Groq, orchestrated by LangChain, to analyze a company's website (landing page and several key sub-pages) and synthesize the information into a cohesive, customer-focused, investor-friendly, and recruiter-relevant brochure summary, delivered in Markdown format.

The application uses LangSmith for tracing and observability, providing a complete view of the LLM pipeline's execution and cost.

Features
URL-Based Analysis: Accepts a root URL and company name as input.

Intelligent Link Filtering: Uses the LLM (link_system_prompt) to determine the most relevant pages (e.g., About Us, Careers, Contact) for deeper content extraction.

Multi-Page Content Aggregation: Simulates scraping content from the landing page and filtered sub-pages.

Brochure Synthesis: Uses the LLM (system_prompt) to synthesize aggregated content into a single, comprehensive marketing brochure summary.

Streamlit UI: Provides an easy-to-use web interface for input and display.

LangSmith Tracing: Configured for full observability of all LLM calls and chain executions (as defined in the Canvas configuration).

Prerequisites
Before running the application, ensure you have the following installed:

Python 3.9+

API Keys:

Groq API Key: For powering the LLM calls (ChatGroq).

LangSmith API Key: For tracing and debugging (Optional, but highly recommended).

Setup and Installation
Clone the repository (or set up your project directory):

mkdir brochure-generator
cd brochure-generator
# Place all Python files (app.py, config.py, web.py, etc.) here

Create a virtual environment:

python -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate

Install dependencies:

pip install streamlit langchain-groq langchain-core python-dotenv
# Note: `WebsiteScrapper` and `logger` dependencies are abstracted, 
# but the necessary libraries for logging and web scraping (like requests/beautifulsoup) 
# should be installed if the mock classes are replaced with real implementations.

Configuration
You must create a file named .env in the root directory to store your sensitive configuration.

The configuration required for this project, including the values selected in the Canvas, is:

# --- Groq API Key ---
# Required for LangChain's ChatGroq to authenticate with the Groq service.
GROQ_API_KEY="your-groq-api-key"

# --- LangSmith Tracing Configuration (As specified in the Canvas) ---
# Enables V2 tracing for LangChain/LangSmith
LANGCHAIN_TRACING_V2="true"

# Your unique API key obtained from LangSmith settings
LANGCHAIN_API_KEY="your-api-key-goes-here"

# The name of the project/application to group traces under
LANGCHAIN_PROJECT="my-brochure-generator"

Running the Application
Ensure your environment is activated and the .env file is configured.

Run the Streamlit application from your terminal:

streamlit run app.py

Access the application at the provided local URL (http://localhost:8501).

Core Workflow Overview
The application executes a multi-step LangChain/LLM workflow:

Setup (setup_environment()): Loads all environment variables (including LangSmith and Groq keys) via python-dotenv.

Link Filtering (get_links(url)):

Calls WebsiteScrapper(url) to get a list of all raw links.

Sends the raw links to the LLM (llm.invoke) using link_system_prompt to identify and categorize brochure-relevant links (about page, careers page, etc.).

Defensively strips markdown fences (````json`) and parses the resulting JSON string.

Content Aggregation (get_all_details(url)):

Retrieves content from the main landing page.

Iterates through the links found in the previous step and retrieves content for each relevant sub-page.

Aggregates all retrieved content into a single long string (truncated at 5,000 characters to prevent excessive token usage).

Brochure Generation (create_brochure):

Sends the massive aggregated content string to the LLM along with the comprehensive system_prompt.

The LLM synthesizes the content into a final, formatted Markdown brochure summary.
