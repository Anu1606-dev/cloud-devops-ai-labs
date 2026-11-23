from pathlib import Path
import re

chunks_dir = Path("../lab2-chunking/chunks")

documents = {}

for file in sorted(chunks_dir.glob("chunk_*.txt")):
    documents[file.name] = file.read_text()

queries = [
    "processor load",
    "available RAM memory",
    "resolve backend hostname DNS",
    "storage full write logs disk",
    "Linux service crashed unavailable",
]

def tokenize(text):
    return set(re.findall(r"\b[a-zA-Z0-9]+\b", text.lower()))

for query in queries:
    query_words = tokenize(query)
    results = []

    for filename, content in documents.items():
        document_words = tokenize(content)
        score = len(query_words & document_words)

        if score > 0:
            results.append((filename, score))

    results.sort(key=lambda item: item[1], reverse=True)

    print(f"\nQuery: {query}")

    if results:
        for filename, score in results:
            print(f"{filename} | Match score: {score}")
    else:
        print("No matching documents found.")
