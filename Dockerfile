# Dockerfile pour l'agent IA
FROM python:3.10-slim

# Dossier de travail
WORKDIR /app

# Copier le script Python
COPY agent_metrics.py .

# Installer la librairie Prometheus client
RUN pip install prometheus_client

# Exposer le port 8000 pour Prometheus
EXPOSE 8000

# Lancer le script quand le container démarre
CMD ["python3", "agent_metrics.py"]
