
#!/bin/bash
echo "Deploying application..."
docker-compose -f docker/docker-compose.yml up --build -d
