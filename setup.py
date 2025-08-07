from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Mlops_Airflow_Redis_Alibi_Grafana",
    version="0.1",
    author="Sandeep",
    packages=find_packages(),
    install_requires = requirements,
)