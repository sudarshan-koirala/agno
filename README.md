# agno
This repo holds the content from my [agno](https://www.agno.com/) youtube playlist
---
## Setup

### 1. Install [uv](https://docs.astral.sh/uv/)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Clone and Initialize
```bash
git clone https://github.com/sudarshan-koirala/agno.git
cd agno
uv sync
```

### 3. Environment Variables
Create a `.env` file:
```bash
cp .env.example .env
# Edit .env with your values
```

Add python-dotenv to load environment variables:
```bash
uv add agno python-dotenv
```

## Usage

### Run your code
```bash
uv run python hello.py
```

### Add packages
```bash
uv add package-name
```

## Project Files
```
.
├── .env              # Your environment variables
├── .env.example      # Example environment file  
├── pyproject.toml    # Project config
├── main.py           # Your main script
└── .venv/            # Virtual environment
```
