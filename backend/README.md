# Timeline FastAPI Backend

Timeline powers a web app that showcases the most trending items across popular categories. Currently, the app highlights four main categories:

- Mobiles
- Clothes
- Beauty
- Gadgets

More categories will be added in the future as the platform grows.

## Project Structure

- `app/` - Main application code
  - `main.py` - FastAPI entry point
  - `api/v1/endpoints/` - API route handlers
  - `models/` - SQLAlchemy models
  - `schemas/` - Pydantic schemas
  - `services/` - Business logic/services
  - `utils/` - Utility functions
  - `core/` - Configuration and core logic

## Setup

1. Make sure you have Python 3.13 or newer installed.
   - You can check your version with:
     ```sh
     python --version
     ```
   - [Download Python](https://www.python.org/downloads/)

2. Install [uv](https://github.com/astral-sh/uv) (if not already installed):
   ```sh
   pip install uv
   ```

3. Install dependencies and set up the environment:
   ```sh
   uv sync
   ```
   - Main dependency: `sqlalchemy`

4. Run the FastAPI server:
   ```sh
   uvicorn app.main:app --reload
   ```

## Example Endpoint

- Visit [http://localhost:8000/api/v1/example](http://localhost:8000/api/v1/example) to see the example endpoint.

## Notes
- Add new backend dependencies to your environment using `uv pip install <package>`.
- Track new packages in a rule file at the project root if required.
