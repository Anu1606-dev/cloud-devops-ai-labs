import re
from pathlib import Path

source_file = Path("knowledge_base.txt")
chunks_dir = Path("chunks")

text = source_file.read_text()

documents = re.split(r"(?=^\[DOC \d+:)", text, flags=re.MULTILINE)

documents = [doc.strip() for doc in documents if doc.strip()]

chunks_dir.mkdir(exist_ok=True)

for i, doc in enumerate(documents, start=1):
    output_file = chunks_dir / f"chunk_{i}.txt"
    output_file.write_text(doc + "\n")
    print(f"Created: {output_file}")

print(f"\nTotal chunks created: {len(documents)}")
