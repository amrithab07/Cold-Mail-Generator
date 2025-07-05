import re

def clean_text(text):
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)

    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)

    # Remove special characters (except spaces and alphanumerics)
    text = re.sub(r'[^a-z0-9\s]', '', text)

    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)

    # Trim leading/trailing whitespace
    text = text.strip()

    return text
