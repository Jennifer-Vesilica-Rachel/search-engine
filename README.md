# IR Search Engine v2

A small IR playground and demo search engine built with **Flask**.  
It indexes a collection of documents (default + user‑uploaded) using an **Inverted Index** and **TF‑IDF**, then ranks results with **cosine similarity** so you can see how classic information retrieval works end‑to‑end.

## Features

- **TF‑IDF + Cosine Similarity search**: ranks documents by semantic relevance to the query.
- **User‑uploaded documents**: upload your own `.txt` files to expand the collection.
- **Document management**: see all indexed documents and delete uploads.
- **Default corpus**: 5 example documents are included so you can try the engine immediately.
- **Transparency**: view intermediate calculation tables — Inverted Index, TF, IDF, TF‑IDF, and Query Vector.

## Screenshots

All project screenshots are stored in the `assets/` folder at the root of this repository (for example `assets/homepage.png`, `assets/documents.png`, etc.).

### Main search interface

![IR Search Engine v2 – Search](https://github.com/Jennifer-Vesilica-Rachel/search-engine/blob/main/assets/IR-Search-Engine-v2-03-04-2026_11_23_PM.png)

### Documents view

![IR Search Engine v2 – Documents](https://github.com/Jennifer-Vesilica-Rachel/search-engine/blob/main/assets/Documents-%E2%80%94-IR-Search-Engine-v2-03-04-2026_11_27_PM.png)

### Flask server running in PyCharm terminal

![IR Search Engine v2 – Full Page](https://github.com/Jennifer-Vesilica-Rachel/search-engine/blob/main/assets/Screenshot%202026-03-04%20225932.png)

## Project Structure

```
search_engine_v2/
├── app.py
├── requirements.txt
├── README.md
├── default_docs/
│   ├── d1.txt
│   ├── d2.txt
│   ├── d3.txt
│   ├── d4.txt
│   └── d5.txt
├── uploads/          ← user uploaded files go here (created at runtime)
└── templates/
    ├── index.html
    └── documents.html
```

## Getting Started

### Prerequisites

- **Python 3.10+**
- `pip` installed and on your `PATH`

### 1. Clone the repository

```bash
git clone https://github.com/Jennifer-Vesilica-Rachel/search-engine.git
cd search-engine-v2
```

> If you downloaded the project in another way, just `cd` into the `search_engine_v2` folder.

### 2. (Optional) Create and activate a virtual environment

**Windows (PowerShell):**

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the development server

```bash
python app.py
```

Then open your browser at **http://127.0.0.1:5000** (or the URL printed in the terminal).

## How It Works

1. Load default + uploaded documents.
2. Preprocess text (lowercasing, stopword removal, basic tokenisation).
3. Build an **Inverted Index** mapping terms to document IDs.
4. Compute **TF**, **IDF**, and **TF‑IDF** weights for each term in each document.
5. Convert the user query into a TF‑IDF vector in the same space.
6. Rank documents by **cosine similarity** to the query vector and display the scores.

## Deployment

The app is deployed on Vercel: `https://search-engine-self-sigma.vercel.app/`
