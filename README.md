# FastAPI CRUD Application
This project is a FastAPI-based CRUD application with MySQL database integration.
## 🚀 Quick Start
### Prerequisites
- Python 3.9+
- Docker and Docker Compose
### Local Development Setup
1. **Create a virtual environment:**
   `
   python3 -m venv fast_crud
   `

2. **Activate the virtual environment:**
`source fast_crud/bin/activate`

3. **Install dependencies:**
`pip install -r requirements.txt`

4. **Start the MySQL database:**
`docker-compose up -d`

5. **Run the application:**
`uvicorn main:app --reload --host 0.0.0.0 --port 8080`

Alternatively, if you're using VS Code, you can use the Python Debugger: FastAPI configuration to run and debug the application.

## 🛠️ Development
* The application will be available at http://localhost:8080.
* API documentation: http://localhost:8080/docs
* ReDoc documentation: http://localhost:8080/redoc

## 📁 Project Structure
.
├── controllers/
│   ├── auth_controller.py
│   └── product_controller.py
├── database.py
├── config.py
├── main.py
├── requirements.txt
├── docker-compose.yml
└── README.md


## 🐳 Docker
The project includes a docker-compose.yml file for easy database setup. To start the MySQL database, run:
`docker-compose up -d`


## 🧪 Testing and Deployment
### Testing
Due to time constraints, comprehensive test setup could not be completed. However, basic tests are available and can be run from the project root using:
```bash
pytest test_product_module.py
```

## Deployment
The project has not been uploaded to a cloud platform. The idea was to upload on Render, but i'm writing this on my last minutes.