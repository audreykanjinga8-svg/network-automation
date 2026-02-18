from prometheus_client import start_http_server, Counter
import random
import time

# Compteurs Prometheus
ia_incidents = Counter("ia_incident_detected_total", "Nombre d'incidents détectés par l'IA")
deployment_success = Counter("deployment_success_total", "Nombre de déploiements réussis")
deployment_failed = Counter("deployment_failed_total", "Nombre de déploiements échoués")

# Exposer le port 8000
start_http_server(8000, addr="0.0.0.0")

while True:
    # Simulation : l'agent détecte un incident aléatoire
    if random.random() < 0.3:
        ia_incidents.inc()
    # Simulation : succès ou échec déploiement
    if random.random() < 0.8:
        deployment_success.inc()
    else:
        deployment_failed.inc()
    time.sleep(5)
