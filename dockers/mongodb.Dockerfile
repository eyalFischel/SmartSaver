# Use the official MongoDB image from Docker Hub
FROM mongo:latest

# Copy the initialization script into the container
COPY backend/mongodb/init-mongo.js /docker-entrypoint-initdb.d/

# Expose the MongoDB default port
EXPOSE 27017




