from setuptools import find_packages, setup
from typing import List

def get_requirements(path: str) -> List[str]:
    """Reads requirements from a file and returns a list of dependencies."""
    with open(path, encoding="utf-8") as f:
        requirements = f.read().splitlines()
    
    # Remove empty lines and '-e .' if present
    requirements = [req for req in requirements if req and not req.startswith('-e')]
    
    return requirements

setup(
    name='mlproject',
    version='0.1',
    author="Subhadip",
    author_email="subhadipmondal789@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
