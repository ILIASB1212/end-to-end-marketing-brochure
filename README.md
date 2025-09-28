# 🚀 AI Marketing Brochure Generator

> *Automating Content Creation with Intelligent AI Analysis*

## 📋 Project Overview

The **AI Marketing Brochure Generator** is a cutting-edge Streamlit application that revolutionizes the initial phase of marketing content creation. By leveraging advanced **Large Language Models (LLMs)** from Groq and orchestrated through **LangChain**, this tool automatically analyzes company websites and generates comprehensive, multi-purpose brochure summaries.

### 🎯 Key Value Proposition

- **Automated Content Synthesis**: Transform website content into professional marketing materials
- **Multi-Audience Focus**: Create content tailored for customers, investors, AND recruiters
- **Intelligent Analysis**: Smart page selection and content aggregation
- **Enterprise-Ready**: Full observability with LangSmith integration

## ✨ Features

### 🔍 **Smart Website Analysis**
- **URL-Based Intelligence**: Input just a root URL and company name
- **Relevant Page Detection**: AI-powered filtering of key pages (About Us, Careers, Contact, etc.)
- **Multi-Page Aggregation**: Comprehensive content extraction across entire website sections

### 🤖 **AI-Powered Content Generation**
- **Groq LLM Integration**: High-speed language model processing
- **Markdown Output**: Clean, formatted brochure summaries
- **Multi-Perspective Content**: Simultaneously addresses:
  - 🎯 **Customer-focused** messaging
  - 💼 **Investor-friendly** insights  
  - 👥 **Recruiter-relevant** information

### 🔧 **Professional Development Stack**
- **LangChain Orchestration**: Robust AI workflow management
- **LangSmith Tracing**: Complete pipeline observability and cost tracking
- **Streamlit UI**: Intuitive web interface for easy usage

## 🛠 Technical Architecture

### Core Workflow

```python
1. URL Input → 2. Smart Link Filtering → 3. Multi-Page Content Aggregation → 4. AI Synthesis → 5. Markdown Brochure Output

📦 Prerequisites
System Requirements:

Python 3.9+

API Keys:

🔑 Groq API Key (LLM processing)

📊 LangSmith API Key (Optional, recommended for tracing)

🚀 Quick Start Guide
1. Environment Setup
bash
# Clone and setup project
mkdir brochure-generator
cd brochure-generator

# Create virtual environment
python -m venv env
source env/bin/activate  # Windows: .\env\Scripts\activate
2. Installation
bash
# Install dependencies
pip install streamlit langchain-groq langchain-core python-dotenv

# Additional libraries for production (if replacing mock classes)
pip install requests beautifulsoup4
3. Configuration
Create .env file in root directory:

env
# --- Groq API Configuration ---
GROQ_API_KEY="your-groq-api-key-here"

# --- LangSmith Tracing (As configured in Canvas) ---
LANGCHAIN_TRACING_V2="true"
LANGCHAIN_API_KEY="your-langsmith-api-key"
LANGCHAIN_PROJECT="my-brochure-generator"
4. Launch Application
bash
streamlit run app.py
📍 Access URL: http://localhost:8501

🔄 Core Workflow Details
Step 1: Environment Setup
Function: setup_environment()

Purpose: Loads all environment variables and API configurations

Technology: python-dotenv for secure credential management

Step 2: Intelligent Link Filtering
Function: get_links(url)

Process:

WebsiteScrapper(url) extracts all raw links

LLM analyzes links using link_system_prompt

JSON parsing with defensive markdown fence stripping

Returns categorized, relevant pages

Step 3: Content Aggregation
Function: get_all_details(url)

Process:

Retrieves main landing page content

Iterates through filtered sub-pages

Aggregates content (truncated at 5,000 characters for token efficiency)

Compiles comprehensive content string

Step 4: Brochure Synthesis
Function: create_brochure()

Process:

Sends aggregated content to LLM with system_prompt

AI synthesizes multi-perspective brochure

Outputs formatted Markdown summary

🎨 Output Example
markdown
# [Company Name] Marketing Brochure

## 🎯 For Customers
- Value proposition and key offerings
- Unique selling points and benefits

## 💼 For Investors  
- Business model and growth potential
- Market position and competitive advantages

## 👥 For Recruiters
- Company culture and values
- Career opportunities and employee value proposition
📊 Monitoring & Observability
LangSmith Integration: Full pipeline tracing

Cost Tracking: Monitor LLM usage and expenses

Performance Metrics: Execution time and token consumption

Debugging Support: Complete visibility into AI decision process

💡 Use Cases
🏢 Enterprise Marketing Teams
Rapid brochure creation for new product launches

Consistent messaging across multiple audience segments

🚀 Startups & SMBs
Professional marketing materials without dedicated content teams

Investor pitch deck supplements

🎓 Marketing Agencies
Scalable content generation for multiple clients

Consistent quality across different industries

🔮 Future Enhancements
Multi-language support

Custom template integration

Brand voice customization

Competitive analysis integration

Automated image suggestion
