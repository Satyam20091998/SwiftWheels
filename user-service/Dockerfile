# Use Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY app/ app/

# Set environment variables
ENV FLASK_APP=app/routes.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the service port
EXPOSE 5001

# Run the application
CMD ["flask", "run", "--port=5001"]
