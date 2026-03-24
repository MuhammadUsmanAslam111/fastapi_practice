# Step 1: Use an official Python image
FROM python:3.10-slim

# Step 2: Set working directory inside container
WORKDIR /app

# Step 3: Copy only requirements first (for caching)
COPY requirements.txt .

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy your application code
COPY . .


# Step 7: Expose port for FastAPI
EXPOSE 8000

# Step 8: Command to run FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
