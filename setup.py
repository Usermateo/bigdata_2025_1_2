from setuptools import setup, find_packages

setup(
    version="0.1.0",
    description="Extraccion de datos de partidos de la Premier League a SQLite3",
    author="Mateo Galvis",
    packages=find_packages(),
    install_requires=[
        "pandas"
    ],
)
