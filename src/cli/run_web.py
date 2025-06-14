import uvicorn


def run_web():
    from src.web import create_app

    uvicorn.run(create_app(), host="0.0.0.0", port=8000)
