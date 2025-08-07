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

#### Download the JSON key from here

<img width="1892" height="787" alt="Image" src="https://github.com/user-attachments/assets/b8c98805-9215-41db-a277-f3ce35efdbb6" />

#### Edit Access --> Add Principal --> Add your Service account number --> Select the same roles
1. `owner`
2. `storage object admin` 
3. `storage object viewer`

<img width="1921" height="838" alt="Image" src="https://github.com/user-attachments/assets/b938ebf7-0dd5-464d-93e0-979c2f6516c0" />

#### setup python workflow

#### Setup Astro
- Download the astro CLI and install
- Add the keys.json in include folder
- Add the deployement code in config under .astro:

``` bash
deployments:
  - name: dev
    executor: celery
    image:
      name: quay.io/astronomer/astro-runtime:7.3.0
    env: dev
    volumes:
      - ./include:/usr/local/airflow/include
```