from rank_bm25 import BM25Okapi

class HybridRetriever:
    def __init__(self, docs, vectorstore):
        self.docs = docs
        self.vectorstore = vectorstore
        self.bm25 = BM25Okapi([doc.page_content.split() for doc in docs])

    def retrieve(self, query):
        # Semantic search
        semantic_docs = self.vectorstore.similarity_search(query, k=3)

        # Keyword search
        tokenized_query = query.split()
        bm25_scores = self.bm25.get_scores(tokenized_query)

        keyword_docs = sorted(
            zip(self.docs, bm25_scores),
            key=lambda x: x[1],
            reverse=True
        )[:3]

        keyword_docs = [doc for doc, _ in keyword_docs]

        return semantic_docs + keyword_docs
