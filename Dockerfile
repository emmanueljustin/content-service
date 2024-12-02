# Use the official Python image with the desired version
FROM python:3.12.5-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Install PostgreSQL dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt into the container
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project into the container
COPY . /app/

# Expose the port your app will run on
EXPOSE 8000

# Set the entry point to start Gunicorn
CMD ["gunicorn", "contentService.wsgi:application", "--bind", "0.0.0.0:8000"]
