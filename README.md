# GitHub Scrapper

A simple Python script to scrape a GitHub user's profile information and repositories, including the README files for each repository.

## Features

- Fetches GitHub user name and bio
- Lists all public repositories
- Downloads the README.md (from `main` or `master` branch) for each repository
- Outputs all data in JSON format

## Requirements

- Python 3.x
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python app.py
```

## Output

The script prints a JSON object with the following structure:

```json
{
  "name": "User Name",
  "bio": "User bio",
  "repositories": [
    {
      "repository": "repo-name",
      "readme": "README contents..."
    }
  ]
}
```

## License

MIT License