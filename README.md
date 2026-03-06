AI Content Repurposing Engine

Project Overview :

The AI Content Repurposing Engine is an intelligent system that converts long-form content such as blogs or articles into multiple platform-specific formats including LinkedIn posts, Twitter threads, YouTube scripts, and newsletter summaries.

The system analyzes the content semantically, extracts key insights, and generates optimized outputs tailored to the tone and style of each platform using Large Language Models.

This allows content creators and marketing teams to efficiently distribute a single piece of content across multiple platforms.

................................................................

System Architecture :

User Input (Blog URL / Text)
            │
            ▼
Content Parsing Module
(parser.py)
Extracts and cleans article text
            │
            ▼
Semantic Analysis Module
(semantic.py)
Creates embeddings and extracts key insights
            │
            ▼
Content Planning Agent
(planner.py)
Decides tone and strategy for each platform
            │
            ▼
Platform Generation Agents
(generators.py)
Uses Groq LLM to generate content for:
   • LinkedIn
   • Twitter
   • YouTube
   • Newsletter
            │
            ▼
Quality Review Agent
(reviewer.py)
Removes duplicates and improves readability
            │
            ▼
Final Output Generator
Displays and saves platform-specific content

........................................................

Core Modules:

1. Content Parser

Extracts text from blog URLs and cleans HTML.
Functions
Extract blog text
Remove navigation, ads, scripts
Split content into logical sections

File: parser.py

2. Semantic Analyzer

Uses SentenceTransformers to generate embeddings and identify key sentences from the blog.

File: semantic.py

Responsibilities:
Generate embeddings
Rank sentences based on importance
Select top key insights

3. Content Planning Agent

Determines the tone and transformation strategy for each platform.

File: planner.py

Example tones:

| Platform   | Tone                  |
| ---------- | --------------------- |
| LinkedIn   | Professional          |
| Twitter    | Concise thread        |
| YouTube    | Conversational script |
| Newsletter | Structured digest     |

4. Platform Generation Agents

Uses Groq LLM API to generate content.

File: generators.py

Supported outputs:
LinkedIn Post
Twitter Thread
YouTube Script
Newsletter Summary

5. Quality Review Agent

Improves the generated content.

File: reviewer.py

Tasks:
Remove duplicate lines
Improve readability
Clean output formatting

Technology Stack:

| Technology           | Purpose                   |
| -------------------- | ------------------------- |
| Python               | Core programming language |
| Streamlit            | User interface            |
| Groq API             | Large language model      |
| SentenceTransformers | Embedding generation      |
| BeautifulSoup        | HTML cleaning             |
| Newspaper3k          | Blog parsing              |
| NumPy                | Vector similarity         |


How to Run the Project :

1. Install dependencies

pip install -r requirements.txt

2. Add Groq API Key

Create .env
Add " GROQ_API_KEY=your_api_key_here " in .env file

3. Run Application
streamlit run app.py

..................................................

Future Improvements :

Automatic hashtag generation
SEO keyword extraction
Batch processing multiple blogs
Tone customization
Character limit enforcement

.......................................................


Author :

AI Content Repurposing Engine Project

.........................................................