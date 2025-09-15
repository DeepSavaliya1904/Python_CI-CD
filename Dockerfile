# Use an official Python runtime as the base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Expose the port Django will run on
EXPOSE 8000

# Run Django development server (replace with gunicorn for production)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]