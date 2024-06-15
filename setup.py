from setuptools import setup, find_packages

setup(
    name="jacked", 
    version="0.1.0",
    author="Joshiwa van Marrewijk",
    author_email="joshiwa01@gmail.com",
    description="Jackknifing interferometric datasets",
    long_description_content_type="text/markdown",
    url="https://github.com/Joshiwavm/jacked", 
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='=3.6',
)