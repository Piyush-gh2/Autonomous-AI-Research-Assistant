import faiss
import numpy as np
from rag.embedder import get_embedding

class VectorStore:
    def __init__(self):
        self.index = None
        self.texts = []

    def build_index(self, documents):
        self.texts = documents
        embeddings = get_embedding(documents)
        dim = embeddings.shape[1]
        
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(np.array(embeddings))

    def search(self, query, k=3):
        query_vec = get_embedding([query])
        distances, indices = self.index.search(query_vec, k)
        
        return [self.texts[i] for i in indices[0]]