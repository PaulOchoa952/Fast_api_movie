# Towatchlist Project

A robust movie watchlist manager built with FastAPI, SQLite, and Docker. Track your movies, mark them as watched, and manage your watchlist efficiently.

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org)

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/Towatchlist.git

# Navigate to project directory
cd Towatchlist

# Run with Docker
docker-compose up --build
```

## 🎯 Features

- ✨ **Movie Management**: Full CRUD operations for your movie watchlist
- 📊 **Status Tracking**: Mark movies as watched/unwatched
- 🔒 **Soft Delete**: Safe deletion with status tracking
- 📝 **Request Logging**: Automatic logging of all HTTP requests
- 🏥 **Health Checks**: Built-in monitoring endpoints
- 🐳 **Docker Support**: Easy deployment with containers

## 🏗️ Project Structure

```
Towatchlist/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application
│   ├── models.py        # Database models
│   ├── schemas.py       # Pydantic schemas
│   ├── crud.py         # Database operations
│   ├── database.py     # Database configuration
│   └── logger.py       # Request logging
├── docker/             # Docker configuration files
├── tests/             # Unit and integration tests
├── .env.example       # Environment variables template
├── docker-compose.yml # Docker compose configuration
├── Dockerfile         # Docker build instructions
└── README.md         # Project documentation
```

## 🛠️ Installation

### Local Development

```bash
# Create virtual environment
python -m venv env

# Activate virtual environment
# Windows:
.\env\Scripts\activate
# Unix/macOS:
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env

# Start the application
uvicorn app.main:app --reload
```

### Docker Deployment

```bash
# Build and start containers
docker-compose up --build

# Stop containers
docker-compose down
```

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/movies` | List all movies |
| POST | `/movies` | Add a new movie |
| GET | `/movies/{id}` | Get movie details |
| PUT | `/movies/{id}` | Update movie details |
| PUT | `/movies/{id}/watched` | Mark as watched |
| DELETE | `/movies/{id}` | Delete a movie |
| GET | `/health` | Check API health |

## 🧪 Testing

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=app tests/
```

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```env
DATABASE_URL=sqlite:///./movies.db
APP_ENV=development
```

## 📚 Documentation

- API Documentation: `http://localhost:8000/docs`
- ReDoc Interface: `http://localhost:8000/redoc`

## 🤝 Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Contact

- Author: Your Name
- Email: alejochoa99@gmail.com
- GitHub: [@PaulOchoa952](https://github.com/PaulOchoa952)