"""Optional GPU accelerator for the course (NVIDIA GPUs).

Why this exists: the Foundry Local CLI daemon (0.10.2) fails to register
GPU execution providers on some machines and then only serves CPU model
builds. This script uses the foundry-local-sdk instead: it registers the
CUDA execution provider, downloads/loads the GPU builds of the course
models, and serves the same OpenAI-compatible API on port 5273.

Usage (leave it running in its own terminal):

    python gpu_server.py

Every week's code picks it up automatically: foundry_client.py checks for
this server first and prefers it over the CPU daemon. Stop it with Ctrl-C
and the code falls back to the CPU daemon on the next run.

Configuration:
- MODELS: keep in sync with config.py if you changed the course models.
- EP: CUDAExecutionProvider is for NVIDIA; on non-NVIDIA GPUs try
  "WebGpuExecutionProvider" (experimental).

Measured on an RTX 5070 Ti: ~180 tokens/s vs ~20 tokens/s on CPU.
"""

import time

from foundry_local_sdk import Configuration, FoundryLocalManager

PORT = 5273

MODELS = ["phi-3.5-mini", "qwen3-embedding-0.6b"]

EP = "CUDAExecutionProvider"


def main():
    cfg = Configuration(
        app_name="foundry",
        web=Configuration.WebService(urls=f"http://127.0.0.1:{PORT}"),
    )
    FoundryLocalManager.initialize(cfg)
    manager = FoundryLocalManager.instance

    print(f"Registering {EP} (first run downloads the GPU runtime, ~2 GB)...")
    result = manager.download_and_register_eps([EP])
    if not result.success:
        raise SystemExit(f"Could not register {EP}: {result.status}")
    print(f"  {result.status}")

    for alias in MODELS:
        model = manager.catalog.get_model(alias)
        variant = next((v for v in model.variants or [] if "cuda" in v.id.lower()), None)
        if variant is None:
            print(f"  {alias}: no CUDA build in the catalog, skipping")
            continue
        if not variant.is_cached:
            print(f"  {alias}: downloading {variant.id} ...")
            variant.download()
        print(f"  {alias}: loading {variant.id} ...")
        variant.load()

    manager.start_web_service()
    print(f"\nGPU service ready on http://127.0.0.1:{PORT}/v1  (Ctrl-C to stop)")
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        print("Stopping.")


if __name__ == "__main__":
    main()
