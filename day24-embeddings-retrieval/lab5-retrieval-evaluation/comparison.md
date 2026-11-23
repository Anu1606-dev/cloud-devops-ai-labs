# Day 24 - Retrieval Evaluation

## 1. Objective
Compare manual, keyword-based, and semantic retrieval
approaches for Linux troubleshooting knowledge.

## 2. Retrieval Approaches

### Manual Retrieval
Human interpretation selects relevant documents.
Effective for small knowledge bases but not scalable.

### Keyword Retrieval
Matches literal words in a query and document.
Effective for exact terms, error codes, and commands.
Can fail when different vocabulary is used.

### Semantic Retrieval
Uses embeddings and cosine similarity to retrieve
documents based on meaning.
Can identify relevant documents despite vocabulary mismatch.

## 3. Experimental Results

| Query | Keyword Search | Semantic Search |
|---|---|---|
| processor load | No match | CPU |
| available RAM memory | Memory | Memory |
| resolve backend hostname DNS | Network | Network |
| storage full write logs disk | Disk, Service | Disk |
| Linux service crashed unavailable | Service, Memory, Network | Service |

## 4. Observations

- Keyword search struggles with vocabulary mismatch.
- Semantic search successfully retrieved CPU for "processor load".
- Semantic search ranked the expected document first for all five queries.
- Secondary semantic results can be less relevant.
- Similarity scores are not confidence percentages.
- Retrieval quality depends on document quality, chunking, the embedding model, and the query.

## 5. Engineering Conclusion

Semantic retrieval is useful when users describe problems differently
from the wording in the knowledge base.

Keyword retrieval remains useful for exact error messages,
CLI commands, identifiers, and error codes.

A production retrieval system may combine keyword and semantic retrieval,
followed by filtering, reranking, and relevance evaluation.

## 6. Day 24 Outcome

Successfully created document chunks, tested keyword retrieval,
generated real embeddings, and evaluated semantic retrieval
using cosine similarity.
