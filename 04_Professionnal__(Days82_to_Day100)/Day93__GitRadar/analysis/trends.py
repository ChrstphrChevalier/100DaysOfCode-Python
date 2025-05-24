from collections import Counter
import re

def count_languages(data: list[dict]) -> dict:
    languages = [repo['language'] for repo in data if repo['language']]
    return dict(Counter(languages))

def top_projects(data: list[dict], top_n: int = 5) -> list[dict]:
    sorted_data = sorted(data, key=lambda x: x['stars'], reverse=True)
    return sorted_data[:top_n]

def find_recurring_words(data: list[dict], top_n: int = 15) -> dict:
    descriptions = [repo['description'] or "" for repo in data]
    all_words = []

    for desc in descriptions:
        words = re.findall(r"\b\w+\b", desc.lower())
        all_words.extend(words)

    known_trends = [
    "ai", "ml", "gpt", "nlp", "llm", "chatbot", "deep", "neural", "model", "training",
    "data", "dataset", "dataframe", "analytics", "etl", "pipeline", "preprocessing", "bigdata",
    "cloud", "aws", "azure", "gcp", "cloudflare", "terraform", "serverless", "kubernetes",
    "docker", "container", "orchestration", "devops", "cicd", "jenkins", "github", "github-actions",
    "api", "rest", "graphql", "webhook", "postman", "swagger", "openapi",
    "web", "frontend", "backend", "fullstack", "html", "css", "javascript", "typescript", "react",
    "vue", "svelte", "nextjs", "nuxt", "astro", "tailwind", "bootstrap",
    "node", "express", "django", "flask", "fastapi", "laravel", "spring", "dotnet", "rails",
    "python", "java", "csharp", "c++", "go", "rust", "php", "ruby", "scala", "typescript",
    "sql", "nosql", "mongodb", "postgresql", "mysql", "sqlite", "redis", "elastic", "dynamodb",
    "aiops", "observability", "prometheus", "grafana", "monitoring", "alerting", "logging", "log",
    "security", "cyber", "auth", "sso", "saml", "oauth", "jwt", "encryption", "zero-trust",
    "pentest", "forensics", "ctf", "malware", "threat", "scanner", "xss", "csrf", "firewall",
    "blockchain", "crypto", "ethereum", "solidity", "nft", "defi", "web3", "metaverse",
    "robotics", "autonomous", "sensor", "embedded", "iot", "firmware", "edge", "raspberry",
    "image", "vision", "detection", "segmentation", "opencv", "audio", "speech", "synthesis", "stt", "tts",
    "reinforcement", "classification", "regression", "clustering", "bayesian", "cnn", "rnn", "transformer",
    "huggingface", "openai", "pytorch", "tensorflow", "sklearn", "xgboost", "lightgbm", "keras",
    "jupyter", "colab", "notebook", "streamlit", "gradio", "dash", "panel",
    "pdf", "ocr", "nlp", "tokenizer", "bert", "embedding", "vector", "faiss", "chroma",
    "rag", "retrieval", "agent", "langchain", "llama", "claude", "anthropic", "cohere", "gemini",
    "search", "crawler", "scraper", "automation", "bot", "cli", "toolkit", "sdk", "framework",
    "game", "gamedev", "unity", "unreal", "engine", "pixel", "sprite", "vr", "ar",
    "test", "unit", "integration", "e2e", "tdd", "bdd", "jest", "pytest", "cypress",
    "design", "ux", "ui", "wireframe", "figma", "adobe", "illustrator", "animation", "canvas",
    "bio", "genome", "protein", "rna", "health", "medical", "medtech", "diagnostic", "simulation", "physics"
    ]


    filtered = [word for word in all_words if word in known_trends]
    return dict(Counter(filtered).most_common(top_n))
