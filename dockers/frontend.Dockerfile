# Use official Node.js image as the base image
FROM node:21-alpine

# Set working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY frontend/package*.json ./

# Install dependencies
RUN npm install

# Copy application code
COPY frontend/ .

# Expose port 3000
EXPOSE 3000

# Command to start Next.js application
CMD ["npm", "run", "dev"]

# TODO set it for production