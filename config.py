# config.py
import os
from dotenv import load_dotenv
from logger.log import logging
def setup_environment():
    load_dotenv()
    os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
    if not os.getenv("LANGCHAIN_API_KEY"):
        raise ValueError("LANGCHAIN_API_KEY is not set in the environment or .env file.")
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    
    os.environ["LANGCHAIN_PROJECT"] = "marketing-brochure-generator"
    
    logging.info("Environment setup complete. LangChain tracing is enabled.")