"""Central configuration for the RAG assistant."""

from pathlib import Path

# Model aliases from the Foundry Local catalog (see `foundry model list`).
CHAT_MODEL = "phi-3.5-mini"           # 2.5 GB — good balance of speed and quality
EMBEDDING_MODEL = "qwen3-embedding-0.6b"  # 495 MB — turns text into 1024-number vectors

# Where the source documents live (shared by all weeks, at the repo root)
# and where this week's SQLite database goes.
DOCS_DIR = Path(__file__).resolve().parents[2] / "sample-docs"
DB_PATH = Path(__file__).resolve().parent / "rag.db"

# Chunking: paragraphs are merged until a chunk reaches about this many characters.
MAX_CHUNK_CHARS = 800

# Retrieval: how many chunks to hand to the model as context.
TOP_K = 3
