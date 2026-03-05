import streamlit as st
from modules import parser, semantic, planner, generators, reviewer

st.set_page_config(page_title="AI Content Repurposing Engine")

st.title("AI Content Repurposing Engine (Groq)")

blog_input = st.text_area("Paste blog text or URL")

platforms = st.multiselect(
    "Select platforms",
    ["linkedin", "twitter", "youtube", "newsletter"],
    default=["linkedin", "twitter"]
)

if st.button("Generate"):
    if not blog_input:
        st.error("Please enter text or URL.")
    else:
        if blog_input.startswith("http"):
            text = parser.extract_text_from_url(blog_input)
        else:
            text = blog_input

        sections = parser.split_into_sections(text)
        key_sentences = semantic.extract_key_sentences(sections)

        plan = planner.create_generation_plan(key_sentences, platforms)
        raw_outputs = generators.generate_platform_content(plan)
        final_outputs = reviewer.quality_check(raw_outputs)

        for platform, content in final_outputs.items():
            st.subheader(platform.capitalize())
            st.text_area(f"{platform} Content", content, height=200)
            st.download_button(f"Download {platform}", content, f"{platform}.txt")