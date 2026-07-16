"""Shared helper: connect to the local Foundry Local service.

Foundry Local exposes an OpenAI-compatible REST API on your own machine.
This module finds that service (starting it if needed), makes sure a model
is loaded into memory, and hands back a standard `openai` client pointed at
it. No cloud, no API key, no internet.

Note: Microsoft's older tutorials use `from foundry_local import
FoundryLocalManager`. That API changed in foundry-local-sdk 1.x, so this
course talks to the service directly through the `foundry` CLI and the
OpenAI-compatible endpoint instead — the approach below works with
Foundry Local 0.10+ and needs only the `openai` package.
"""

import json
import subprocess
import urllib.request

from openai import OpenAI

# Served by the optional tools/gpu_server.py (GPU machines). When it is
# running, all course code automatically uses the GPU instead of the CPU.
GPU_SERVER_URL = "http://127.0.0.1:5273"

# Set by get_service_url(): True when we're talking to the GPU server.
_gpu_mode = False


def _run_foundry(*args):
    """Run a `foundry` CLI command and return its stdout."""
    try:
        result = subprocess.run(
            ["foundry", *args],
            capture_output=True,
            check=True,
            # The foundry CLI prints UTF-8 (progress symbols); decode it as
            # such no matter what the console's own encoding is.
            encoding="utf-8",
            errors="replace",
        )
    except FileNotFoundError:
        raise SystemExit(
            "The 'foundry' command was not found.\n"
            "Install Foundry Local first — see SETUP.md at the repo root."
        )
    except subprocess.CalledProcessError as error:
        raise SystemExit(
            f"'foundry {' '.join(args)}' failed:\n{error.stderr or error.stdout}"
        )
    return result.stdout


def get_service_url():
    """Return the base URL of the local service, starting the daemon if needed.
    Prefers the optional GPU server (tools/gpu_server.py) when it is running."""
    global _gpu_mode
    try:
        with urllib.request.urlopen(GPU_SERVER_URL + "/v1/models", timeout=0.5):
            _gpu_mode = True
            return GPU_SERVER_URL
    except OSError:
        _gpu_mode = False  # GPU server not running - use the regular CPU daemon

    status = json.loads(_run_foundry("server", "status", "-o", "json"))
    if not status.get("running"):
        print("Starting the Foundry Local service...")
        _run_foundry("server", "start")
        status = json.loads(_run_foundry("server", "status", "-o", "json"))
    return status["webUrls"][0]


def get_client():
    """Return an OpenAI client connected to the local service."""
    return OpenAI(base_url=get_service_url() + "/v1", api_key="not-needed")


def resolve_model_id(client, alias):
    """Map a model alias (e.g. 'phi-3.5-mini') to the exact id the service
    expects (e.g. 'Phi-3.5-mini-instruct-generic-cpu'), making sure the
    model is loaded into memory."""

    def matching_ids():
        return [
            model.id
            for model in client.models.list()
            if alias in (getattr(model, "parent", None), model.id)
            or model.id.lower().startswith(alias.lower())
        ]

    if _gpu_mode:
        # tools/gpu_server.py loads the GPU builds at startup; pick those.
        gpu = [i for i in matching_ids() if "cuda" in i.lower()]
        if gpu:
            return gpu[0]
        raise SystemExit(
            f"Model '{alias}' is not served by the GPU server.\n"
            f"Add it to MODELS in tools/gpu_server.py and restart the server."
        )

    # CPU daemon. Note: its /v1/models endpoint lists every CACHED model,
    # including ones not currently in memory - so always ask the daemon to
    # load (a fast no-op if already loaded; downloads the model first time).
    print(f"Making sure model '{alias}' is loaded...")
    _run_foundry("model", "load", alias)
    cpu = [i for i in matching_ids() if "cuda" not in i.lower()]
    if cpu:
        return cpu[0]
    raise SystemExit(
        f"Model '{alias}' could not be loaded.\n"
        f"Try running: foundry model download {alias}"
    )
