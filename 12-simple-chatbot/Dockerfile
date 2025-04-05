# Use official Python image
FROM python:3.10

# Set working directory inside the container
WORKDIR /app

# Copy only necessary files first (to speed up builds)
COPY pyproject.toml README.md /app/

# Install dependencies using pip
RUN pip install --no-cache-dir .

# Create the required directory and set proper permissions
RUN mkdir -p /app/.files && chmod -R 777 /app/.files

# Copy the rest of the project files
COPY . /app

# Ensure the container runs as root (if necessary)
USER root

# Expose the required port
EXPOSE 7860

# Run the chatbot
CMD ["chainlit", "run", "src/main.py", "--port", "7860", "--host", "0.0.0.0"]
