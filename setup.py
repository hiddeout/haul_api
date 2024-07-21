from setuptools import setup 

with open("requirements.txt") as f: 
    requirements = f.read().splitlines()

setup(
    name="HaulAPI",
    version="1.0.0",
    description="A Python API wrapper for Haul api",
    author="Resent",
    url="https://github.com/evictbot/kure.api",
    install_requires=requirements,
    python_requires='>=3.11.0',
    project_urls = {
        "Documentation": "https://api.haul.digital/"
    }
)
