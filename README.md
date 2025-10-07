This folder contains sanitized copies of my LangChain learning project.

What I did:
- Removed hard-coded API keys and replaced them with environment variable placeholders.
- Added a `.env.example` showing required environment variables.
- Excluded `CV_new_.pdf` from upload for privacy. If you want to include a redacted PDF, replace it manually.

How to use:
1. Copy `.env.example` to `.env` and set your real keys locally (do NOT commit `.env`).
2. Install dependencies from the original `requirements.txt`.
3. Run the scripts as needed.

Notes on sensitive files:
- `CV_new_.pdf` was excluded to protect personal information. Consider removing or redacting before uploading.
- Notebooks had hard-coded os.environ assignments — these were commented out and replaced with placeholders.
