# GitHub Scraper API

A FastAPI-based backend for fetching and summarizing GitHub repository profiles.

## Features

- Fetches GitHub repository profile data via a simple API.
- CORS enabled for frontend integration (e.g., React on `localhost:3000`).
- Easy to extend with additional routes.

## Requirements

- Python 3.8+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/github-scrapper.git
   cd github-scrapper
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Server

Start the FastAPI server with Uvicorn:

```bash
uvicorn main:app --reload --port 8000
```

- The API will be available at [http://localhost:8000](http://localhost:8000).

## API Endpoints

### `GET /api/readme`

Fetch GitHub repository profile data.

**Query Parameters:**
- `repo` (string, required): The repository in the format `owner/repo_name` (e.g., `torvalds/linux`).

**Example Request:**
```
GET http://localhost:3000/api/readme?repo=https://github.com/K-is-SAD
```

**Example Response:**
```json
{
  "name": "linux",
  "bio": "Linux kernel source tree",
  "repositories":[
    {"repo":, "readme":},
    {},
    {},
    
  ]
  ...
}
```

### `GET /`

Health check endpoint.

**Response:**
```json
{ "message": "Hello World" }
```

## Frontend Integration

If you have a frontend running on `localhost:3000`, you can fetch data like this:

```js
fetch("http://localhost:3000/api/readme?repo=https://github.com/K-is-SAD")
  .then(res => res.json())
  .then(data => console.log(data));
```

## License

MIT