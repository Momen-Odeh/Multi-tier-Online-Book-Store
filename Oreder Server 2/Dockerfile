# Use an official Python image as the base
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy the Flask app and requirements file
COPY . /app

# Install Python dependencies, including flask_cors
RUN pip install flask flask_cors requests gunicorn

# Expose the Flask app port
EXPOSE 5002

# Command to run the Flask app
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:5002"]
