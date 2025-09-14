# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Install dependencies
COPY pyproject.toml uv.lock ./
RUN pip install --no-cache-dir uv \
    && uv pip install --system --no-cache .

# Copy app files
COPY . .

# Expose port
EXPOSE 8000

# Run the FastAPI app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
