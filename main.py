import streamlit as st
from scrape import scrape_website, clean_body_content, split_dom_content, extract_body_content
from parse import parse_with_ollama

st.title("AI Web Scraper")
url = st.text_input("Enter a website URL: ")

if st.button("Scrape Site"):
    st.write("Scraping data...")
    result = scrape_website(url)
    body_content = extract_body_content(result)
    clean_content = clean_body_content(body_content)

    st.session_state.dom_content = clean_content

    with st.expander("view DOM Content"):
        st.text_area("DOM Content", value=clean_content, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Descriptive what you want to parse?")

    if st.button("Parse content"):
        if parse_description:
            st.write("Parsing the content")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)
