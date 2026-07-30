# Automated Code Review Bot

Automatically reviews every pull request using Google's Gemini API, posting AI-generated feedback as a comment directly on the PR — no server to host, triggered entirely through GitHub Actions.

Project #2 in a 19-project AI engineering learning sequence. Builds on project #1's "call an LLM API" pattern by adding a second real API (GitHub's REST API) and an automated trigger (GitHub Actions / webhooks), instead of running on-demand from the command line.

## How it works

1. A pull request is opened or updated on this repo
2. GitHub Actions automatically spins up, checks out the code, and runs `reviewer.py`
3. The script fetches the PR's diff from GitHub's API
4. The diff is sent to Gemini with a prompt asking it to flag bugs/issues in the added lines
5. The review is posted back as a comment on the PR, automatically

## Setup (to run this on your own repo)

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install google-genai python-dotenv requests
```

Add `GEMINI_API_KEY` as a **repository secret** (Settings → Secrets and variables → Actions), not just a local `.env` — the script runs on GitHub's servers via Actions, not your machine.

The workflow file (`.github/workflows/review.yml`) is already wired to trigger on every PR — no manual setup beyond adding the secret.

## Stack

Python, Gemini API (`google-genai`), GitHub REST API (`requests`), GitHub Actions

## What this taught me

- Working with a second real API (GitHub's) alongside an LLM API, using raw HTTP calls instead of an SDK
- GitHub Actions — workflow triggers, jobs, steps, and secrets in a CI context (different from local `.env` secret management)
- Automating a task around an event (a PR opening) instead of running it manually on demand
- A review-focused prompting style, distinct from the summarization prompt in project #1
