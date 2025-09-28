from prompt import system_prompt, link_system_prompt
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
import os
import json
from web import WebsiteScrapper
import streamlit as st
from config import setup_environment
from logger.log import logging

setup_environment()

def get_links_user_prompt(website):
    user_prompt = f"Here is the list of links on the website of {website.url} - "
    user_prompt += "please decide which of these are relevant web links for a brochure about the company, respond with the full https URL in JSON format. \
    Do not include Terms of Service, Privacy, email links.\n"
    user_prompt += "Links (some might be relative links):\n"
    user_prompt += "\n".join(website.links)
    return user_prompt


llm=ChatGroq(model="openai/gpt-oss-120b",temperature=1,max_tokens=5000)


def get_links(url):
    website = WebsiteScrapper(url)
    messages = [
        SystemMessage(content=link_system_prompt),
        HumanMessage(content=get_links_user_prompt(website))
    ]
    ai_message = llm.invoke(messages)

    result_json_string = ai_message.content.strip()

    if result_json_string.startswith('```json'):
        result_json_string = result_json_string.lstrip('```json').rstrip('```').strip()
    try:
        return json.loads(result_json_string)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON from Groq response: {e}")
        print(f"Raw response was: {result_json_string}")
        return {"error": "Failed to parse JSON response. Check raw response for model deviation."}


def get_all_details(url):
    result = "Landing page:\n"
    result += WebsiteScrapper(url).get_contents()
    links = get_links(url)
    print("Found links:", links)
    for link in links["links"]:
        result += f"\n\n{link['type']}\n"
        result += WebsiteScrapper(link["url"]).get_contents()
    return result

def get_brochure_user_prompt(company_name, url):
    user_prompt = f"You are looking at a company called: {company_name}\n"
    user_prompt += f"Here are the contents of its landing page and other relevant pages; use this information to build a detailed brochure of the company in markdown.\n"
    user_prompt += get_all_details(url)
    user_prompt = user_prompt[:5_000] 
    return user_prompt


def create_brochure(company_name, url):
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=get_brochure_user_prompt(company_name, url))
    ]
    response = llm.invoke(messages)
    
    return response.content



st.title("AI Marketing Brochure Generator")
st.write("Enter the URL and the name of a company website and get a marketing brochure in markdown format.")
title = st.text_input("Enter company name URL", "NVIDIA")
url = st.text_input("Enter company website URL", "https://www.nvidia.com")
if title and url and url.startswith("http") and ".com" in url:
    try:
        if st.button("Generate Brochure"):
            try:
                with st.spinner("Generating brochure..."):
                    website = WebsiteScrapper(url)
                    brochure = create_brochure(title, url)
                    st.write("### Brochure")
                    st.markdown(brochure)
                    logging.info(f"company name -->{title} \ncontent -->{brochure}")
            except Exception as e:
                st.error(f"An error occurred during brochure generation: {e}")
    except Exception as e:
        st.error(f"An error occurred in link or name: {e}")
        logging.info(f"Brochure generated for {title} at {url}")