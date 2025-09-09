# Install a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install Flask Flask-SQLAlchemy

# Project structure
todo-app/
    app/
        __init__.py
        templates/
        static/
        models.py
        routes.py
    instance/
        task.db
    venv/
    .gitignore
    run.py
