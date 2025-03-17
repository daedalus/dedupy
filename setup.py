from setuptools import setup, find_packages

# Read the content of README file for the long description
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="dedupy",  # Project name
    version="0.1.0",  # Version of your package
    author="Darío Clavijo",  # Your name
    author_email="clavijodario@gmail.com",  # Your email address
    description="A Python package for efficiently deduplicating data in various formats",  # Short description
    long_description=long_description,  # Detailed description from README
    long_description_content_type="text/markdown",  # Content type of the long description
    url="https://github.com/daedalus/dedupy",  # URL of the project repository
    packages=find_packages(where="src"),  # Find packages in the src directory
    package_dir={"": "src"},  # Tells setuptools that packages are inside the src directory
    classifiers=[
        "Programming Language :: Python :: 3",  # Python 3 compatibility
        "License :: OSI Approved :: MIT License",  # License type (change if necessary)
        "Operating System :: OS Independent",  # Operating system compatibility
    ],
    python_requires='>=3.6',  # Minimum required Python version
    install_requires= [line.strip() for line in open(".requirements.txt","r")]
    extras_require={},
    entry_points={  # Entry point for the command line tools (if applicable)
        "console_scripts": [
            "dedupy=src.main:main",  # Replace with your entry function if applicable
        ],
    },
)

