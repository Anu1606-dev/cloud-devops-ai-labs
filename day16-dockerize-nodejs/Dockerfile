
# Use Node.js Alpine as the base image
FROM node:22-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy dependency manifests first
COPY package*.json ./

# Install production dependencies
RUN npm ci --omit=dev

# Copy application source code
COPY app.js ./

# Document the application port
EXPOSE 3000

# Start the Node.js application
CMD ["node", "app.js"]
