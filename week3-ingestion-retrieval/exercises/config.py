"""Central configuration for the RAG assistant.

Settings:
- CHAT_MODEL: model alias from the Foundry Local catalog (see
  `foundry model list`). phi-3.5-mini (2.5 GB) balances speed and quality;
  on a slow machine switch to qwen2.5-0.5b (822 MB).
- EMBEDDING_MODEL: turns text into 1024-number vectors (495 MB).
- DOCS_DIR: the source documents, shared by all weeks at the repo root.
- DB_PATH: where this week's SQLite database goes.
- MAX_CHUNK_CHARS: paragraphs are merged until a chunk reaches roughly
  this many characters.
- TOP_K: how many retrieved chunks are handed to the model as context.
"""

from pathlib import Path

CHAT_MODEL = "phi-3.5-mini"
EMBEDDING_MODEL = "qwen3-embedding-0.6b"

DOCS_DIR = Path(__file__).resolve().parents[2] / "sample-docs"
DB_PATH = Path(__file__).resolve().parent / "rag.db"

MAX_CHUNK_CHARS = 800

TOP_K = 3
