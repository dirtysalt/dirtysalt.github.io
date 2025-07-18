import requests
from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator
import os

# --- Configuration ---
OUTPUT_RSS_FILE = os.path.join(os.path.dirname(__file__), "articles.xml")

def fetch_database_doctor_articles():
    """Fetches articles from database-doctor.com."""
    BLOG_URL = "https://www.database-doctor.com/posts/"
    articles = []
    print(f"Fetching articles from: {BLOG_URL}")
    try:
        response = requests.get(BLOG_URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        for article_link in soup.select('a[href^="/posts/"][href$="html"]'):
            url = f"https://www.database-doctor.com{article_link['href']}"
            title = article_link.get_text(strip=True)
            if title:
                articles.append({"title": title, "link": url})
    except requests.exceptions.RequestException as e:
        print(f"Error fetching from {BLOG_URL}: {e}")
    return articles

def fetch_tomrenner_articles():
    """Fetches articles from tomrenner.com."""
    BLOG_URL = "https://tomrenner.com/posts/"
    articles = []
    print(f"Fetching articles from: {BLOG_URL}")
    try:
        response = requests.get(BLOG_URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        for article_link in soup.select('h1.f3 a'):
            url = f"https://tomrenner.com{article_link['href']}"
            title = article_link.get_text(strip=True)
            if title:
                articles.append({"title": title, "link": url})
    except requests.exceptions.RequestException as e:
        print(f"Error fetching from {BLOG_URL}: {e}")
    return articles

def generate_rss_feed(all_articles):
    """Generates an RSS feed from the collected articles."""
    fg = FeedGenerator()
    fg.id('urn:uuid:60a76c80-d399-11d9-b93C-000389b7c000') # Example UUID, can be anything unique
    fg.title('Combined Blog Feed')
    fg.link( href='http://example.com', rel='alternate' ) # Replace with a relevant link if available
    fg.description('A combined RSS feed of articles from various blogs.')
    fg.language('en')

    # Sort articles by title for consistent output (optional)
    all_articles.sort(key=lambda x: x['title'])

    for article in all_articles:
        fe = fg.add_entry()
        fe.id(article['link'])
        fe.title(article['title'])
        fe.link(href=article['link'])
        # No content needed as per request

    return fg.rss_str(pretty=True)

if __name__ == "__main__":
    # Ensure feedgen is installed
    try:
        import feedgen
    except ImportError:
        print("feedgen not found. Installing...")
        os.system("pip install feedgen")
        import feedgen # Try importing again after install

    all_articles = []
    all_articles.extend(fetch_database_doctor_articles())
    all_articles.extend(fetch_tomrenner_articles())

    if all_articles:
        rss_content = generate_rss_feed(all_articles)
        with open(OUTPUT_RSS_FILE, "wb") as f:
            f.write(rss_content)
        print(f"RSS feed generated successfully at: {OUTPUT_RSS_FILE}")
    else:
        print("No articles found to generate RSS feed.")
