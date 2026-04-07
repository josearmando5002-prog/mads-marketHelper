from pathlib import Path
from setuptools import find_packages, setup

BASE_DIR = Path(__file__).parent.resolve()

try:
    README = (BASE_DIR / "README.md").read_text(encoding="utf-8")
except FileNotFoundError:
    README = "Módulo para gestão e análise de compras, lojas e evolução de preços."

setup(
    name="mads-market-helper",
    version="1.0.2",
    description="Sistema de gestão e análise de compras em superfícies comerciais",
    long_description=README,
    long_description_content_type="text/markdown",
    author="João Martins, José Mendonça, Rodrigo Santos, Mário Pinto",
    author_email="geral@markethelper.com",
    url="https://github.com/josearmando5002-prog/mads-marketHelper", 
    project_urls={
        "Source": "https://github.com/josearmando5002-prog/mads-marketHelper",
        "Issues": "https://github.com/josearmando5002-prog/mads-marketHelper/issues",
    },
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.9",
    install_requires=[
        "matplotlib>=3.7.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    license="MIT",
    keywords="analytics compras lojas estatisticas precos matplotlib",
)
