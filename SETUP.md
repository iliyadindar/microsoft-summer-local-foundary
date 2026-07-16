# Environment Setup

Do this once, in Week 1. Budget ~30 minutes plus model download time.

## 1. Python 3.10 or newer

Check: `python --version`. Install from [python.org](https://www.python.org/downloads/)
if needed (on Windows, tick "Add python.exe to PATH").

## 2. Foundry Local

**Windows:**

```
winget install Microsoft.FoundryLocal
```

**macOS (Apple silicon):**

```
brew tap microsoft/foundrylocal
brew install foundrylocal
```

Then **open a new terminal** (PATH refresh) and check:

```
foundry --version
foundry server status
```

If the server isn't running: `foundry server start`.

## 3. Download the course models

Do this on good Wi-Fi — it's ~3 GB total, one time only:

```
foundry model download phi-3.5-mini
foundry model download qwen3-embedding-0.6b
```

Low-spec laptop? Also grab the lightweight fallback chat model (822 MB):

```
foundry model download qwen2.5-0.5b
```

## 4. Python packages

From the repo root:

```
pip install -r requirements.txt
```

(Consider a virtual environment: `python -m venv .venv` then activate it —
your instructor will demo this.)

## 5. Verify everything

```
foundry model run phi-3.5-mini
```

Type a message; you should get a reply generated on your own machine. Exit
with `/exit`. Then prove Python can reach it too:

```
cd week1-rag-and-setup/solutions
python hello_model.py
```

Expected output: a connected-model line and a short model-written greeting.

## Optional: GPU acceleration (NVIDIA)

Have an NVIDIA GPU? The course runs ~10x faster on it (measured: ~180
tokens/s on an RTX 5070 Ti vs ~20 tokens/s on CPU). Foundry Local 0.10.2's
daemon fails to register GPU support on some machines (it then lists only
CPU builds in `foundry model list`), so the course ships a workaround:

```
pip install foundry-local-sdk
cd tools
python gpu_server.py
```

First run downloads the CUDA runtime (~2 GB) plus GPU builds of the course
models (~2.5 GB), then serves them on port 5273. **Leave it running in its
own terminal.** All course code detects it automatically and prefers it; stop
it with Ctrl-C and everything falls back to the CPU daemon. On non-NVIDIA
GPUs, edit `EP` in the script to `"WebGpuExecutionProvider"` (experimental).

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `foundry` is not recognized | Open a NEW terminal; on Windows re-run the winget install if it persists |
| Older docs mention `foundry service ...` | The command group is `foundry server ...` in current versions |
| `pip install foundry-local-sdk` examples from tutorials fail | Expected — SDK 1.x changed its API. This course doesn't need the SDK; the provided `foundry_client.py` uses the CLI + `openai` package instead |
| First question takes forever | Model loading into RAM takes 10–30 s once per session; later answers take seconds |
| Everything is slow | Edit `config.py`: set `CHAT_MODEL = "qwen2.5-0.5b"` |
| `Database not found` | Run `python ingest.py` before `main.py` / `retrieve.py` |
