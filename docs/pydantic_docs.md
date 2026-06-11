# Pydantic Documentation

## What is Pydantic?

Pydantic is a Python library used for data validation and settings management.

## BaseModel

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
```

## Validation

```python
user = User(
    name="John",
    age=25
)
```

## FastAPI Integration

FastAPI uses Pydantic models to validate request and response data.

Example:

```python
from pydantic import BaseModel

class QueryRequest(BaseModel):
    question: str
```

## Benefits

- Data validation
- Type safety
- Serialization
- Better error handling