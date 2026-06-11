# FastAPI Documentation

## What is FastAPI?

FastAPI is a modern, high-performance web framework for building APIs with Python.

Key Features:
- Fast performance
- Automatic interactive API documentation
- Data validation using Pydantic
- Async support

## Creating an API

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}
```

## Running FastAPI

Use uvicorn:

```bash
uvicorn main:app --reload
```

## Path Parameters

```python
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}
```

## Query Parameters

```python
@app.get("/search")
def search(q: str):
    return {"query": q}
```