# MLOps_Airflow_Redis_Grafana
This MLOps Project involves Airflow, Redis, Alibi, GCP, Grafana, Prometheus

### Tools Used:

1. **ETL Pipeline** – Astro Airflow + PostgreSQL
2. **Feature Store** – Redis via Docker
3. **Drift Detection** – Alibi Detect
4. **ML Monitoring** – Prometheus + Grafana
5. **Cloud** – GCP


### GCP Bucket Creation

<img width="1900" height="717" alt="Image" src="https://github.com/user-attachments/assets/8ca0b80b-2675-4c33-bf11-2d37dad12a3e" />

#### IAM --> Service account --> Add roles as 
1. `owner`
2. `storage object admin` 
3. `storage object viewer`

<img width="1903" height="782" alt="Image" src="https://github.com/user-attachments/assets/f0c7595e-9b0e-4762-a991-5655d5e45757" />