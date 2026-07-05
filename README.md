
# Enterprise Cloud Banking Platform

This is a Cloud Engineer portfolio project including:

- Python Flask API
- Docker containerization
- Docker Compose setup
- GitHub Actions CI pipeline
- Terraform AWS EC2 example
- Linux deployment scripts

## Run locally

```bash
pip install -r requirements.txt
python app/main.py
```

## Run with Docker

```bash
docker-compose -f docker/docker-compose.yml up --build
```

## CI/CD

Push to `main` triggers GitHub Actions pipeline.

## Terraform

```bash
cd terraform
terraform init
terraform apply
```
