FROM mongo:latest

# Set environment variables for MongoDB credentials
ENV MONGO_INITDB_ROOT_USERNAME=${MONGO_USERNAME}
ENV MONGO_INITDB_ROOT_PASSWORD=${MONGO_PASSWORD}

# Create a new database and collection
ENV MONGO_INITDB_DATABASE=mydatabase
ENV MONGO_INITDB_COLLECTION=images

# Copy the initialization script to the container
COPY init.js /docker-entrypoint-initdb.d/

# Set the execution permissions for the initialization script
RUN chmod +x /docker-entrypoint-initdb.d/init.js