# Complaints Microservice

## For running on development:

- Recommended python version: 3.11

1. Create enviroment:

```bash
python -m venv env
```

2. Activate enviroment:

On Windows:

```bash
env\Scripts\activate
```

On Unix or MacOS:

```bash
source env/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Do the database migration

```bash
python3 -m app.infrastructure.configs.migrate_database
```

4. Run the server

```bash
uvicorn app.main:app --reload
```

5. Check for API docs at:

http://127.0.0.1:8000/docs
