from setuptools import setup, find_packages

setup(
    name="argflow",                
    version="1.0.2",               
    packages=find_packages(),      
    install_requires=[],           
    python_requires=">=3.12",       
    url="https://github.com/tu_usuario/argflow",
    author="alesisce",
    description='The easier and "faster" alternative to argparse.',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
