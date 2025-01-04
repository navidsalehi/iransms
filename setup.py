from setuptools import setup, find_packages

setup(
    name="iransms",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "django",
    ],
    description="A Python package to send SMS via multiple Iranian providers",
    author="Navid salehi pour",
    author_email="navid.lord@gmail.com",
    url="https://github.com/navidsalehi/iransms",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
