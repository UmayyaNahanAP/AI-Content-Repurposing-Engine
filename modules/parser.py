from newspaper import Article
from bs4 import BeautifulSoup

def extract_text_from_url(url: str) -> str:
    article = Article(url)
    article.download()
    article.parse()
    return article.text

def clean_text(raw_html: str) -> str:
    soup = BeautifulSoup(raw_html, 'html.parser')
    for script in soup(["script", "style"]):
        script.extract()
    return soup.get_text(separator="\n")

def split_into_sections(text: str):
    sections = [s.strip() for s in text.split("\n\n") if s.strip()]
    return sections