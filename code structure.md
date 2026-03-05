AI-Content-Repurposing-Engine/
│
├─ app.py                 # Streamlit main app
├─ requirements.txt       # All dependencies
├─ .env                   # Store GROQ_API_KEY
├─ README.md              # Project overview + architecture diagram
├─ prompts/
│   └─ templates.json     # Platform-specific prompt templates
├─ outputs/
│   └─ (generated content saved here)
├─ examples/
│   └─ sample_blog.txt    # Sample blog text for testing
└─ modules/
    ├─ parser.py          # Blog parsing (URL/text)
    ├─ semantic.py        # Semantic analysis & embeddings
    ├─ planner.py         # Content planning agent
    ├─ generators.py      # Platform-specific content generation using Groq
    └─ reviewer.py        # Quality review agent