from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="iransms",
    version="0.1.0",  # Update this for each release
    author="Navid Salehi pour",
    author_email="navid.lord@gmail.com",
    description="A Python package to send SMS via multiple Iranian providers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/navidsalehi/iransms",
    packages=find_packages(),
    install_requires=[
        "requests>=2.26.0",
        "django>=3.2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)