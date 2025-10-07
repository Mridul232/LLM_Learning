# LLM Learning

A curated collection of LangChain learning materials, example scripts and notebooks created while following tutorials and practical exercises.

This repository contains sanitized versions of the author's experiments. Hard-coded API keys and private personal files (CV) have been removed or excluded. See `.env.example` for environment variables required to run the examples.

Contents
- `learning/` — Sanitized code, notebooks, and examples used for learning LangChain.
- `.env.example` — Example environment variables (DO NOT commit your real `.env`).
- `push_to_github.ps1` — Helper script to create and push the repo using GitHub CLI.

Quickstart
1. Clone the repo:
```powershell
git clone https://github.com/Mridul232/LLM_Learning.git
cd LLM_Learning
```
2. Copy `.env.example` to `.env` and add your real API keys locally:
```powershell
copy .env.example .env
notepad .env
```
3. Create and activate a virtual environment and install dependencies:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r learning/requirements.txt
```
4. Run examples from the `learning` folder. Notebooks are provided for interactive exploration.

Security
- Never commit your `.env` or real API keys. `.gitignore` is configured to ignore `.env`.
- If a key is accidentally committed, rotate it immediately.

Contributing
Contributions are welcome — please read CONTRIBUTING.md for guidelines.

License
This project is licensed under the MIT License. See LICENSE for details.
