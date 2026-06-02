import pandas as pd
import chromadb
import uuid
from pathlib import Path


class Portfolio:
    def __init__(self):
        base_dir = Path(__file__).parent
        self.file_path = base_dir / "resource" / "my_portfolio.csv"

        self.data = pd.read_csv(self.file_path)

        self.chroma_client = chromadb.PersistentClient(path="vectorstore")
        self.collection = self.chroma_client.get_or_create_collection(
            name="portfolio"
        )

    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(
                    documents=[row["Techstack"]],
                    metadatas=[{"links": row["Links"]}],
                    ids=[str(uuid.uuid4())]
                )

    def query_links(self, skills):
        return self.collection.query(
            query_texts=skills,
            n_results=2
        ).get("metadatas", [])