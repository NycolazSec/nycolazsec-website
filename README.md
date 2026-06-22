# TryWarz Web

This repository contains the source code for TryWarz Web, a web application built using the Flask framework.

## Technologies Used

*   **Backend**: Python 3 with Flask
    *   `Flask`: The web framework.
    *   `Gunicorn`: A Python WSGI HTTP Server for UNIX, used to serve the Flask application.
    *   `PyMySQL`: Python client for MySQL database.
    *   `Flask-Limiter`: Adds rate limiting to Flask routes.
*   **Frontend**: HTML5, CSS3 (main.css), JavaScript (main.js)
*   **Containerization**: Docker, Docker Compose
*   **Orchestration**: Kubernetes (configuration files provided in `k8s/`)

## Setup and Installation

### Using Docker Compose (Recommended)

The easiest way to get the application running is by using Docker Compose.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/trywarz-web.git
    cd trywarz-web
    ```
2.  **Build and run the containers:**
    ```bash
    docker-compose up --build -d
    ```
    This command will build the Docker image, set up the necessary services (including the Flask application and potentially a database if configured in `docker-compose.yml`), and run them in detached mode.

3.  **Access the application:**
    The application should be accessible in your web browser, typically at `http://localhost`.

### Local Development (Python)

If you prefer to run the application directly using Python, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/trywarz-web.git
    cd trywarz-web
    ```
2.  **Create a virtual environment and activate it:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Flask application:**
    ```bash
    python app.py
    ```
    The application will run on `http://127.0.0.1:5000` by default (check console output for exact address).

## Directory Structure

*   `app.py`: The main Flask application entry point.
*   `config/`: Contains configuration files, e.g., `database.py`.
*   `routes/`: Defines the various routes and their logic for the web application.
*   `static/`: Stores static assets like CSS, JavaScript, images, and audio.
*   `templates/`: Contains HTML template files rendered by Flask.
*   `requirements.txt`: Lists all Python dependencies required by the project.
*   `Dockerfile`: Defines the Docker image for the application.
*   `docker-compose.yml`: Defines multi-container Docker applications.
*   `k8s/`: Kubernetes deployment configuration files.
*   `tests/`: Unit and integration tests.

---

**Disclaimer:**

It is strictly forbidden to use, reproduce, or distribute the script(s) and associated code within this repository for any unauthorized purpose without explicit written permission from the owner. This includes, but is not limited to, deployment on external servers, integration into other projects, or any form of commercial exploitation. Violation of this disclaimer may result in legal action.
