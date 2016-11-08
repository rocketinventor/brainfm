""" Setup file """
import os

from setuptools import find_packages, setup


HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, "README.rst")) as f:
    README = f.read()


def get_version():
    with open(os.path.join(HERE, "brainfm.py")) as f:
        for line in f:
            if line.startswith("__version__"):
                return eval(line.split("=")[-1])

if __name__ == "__main__":
    setup(
        name="brainfm",
        version=get_version(),
        description="Unofficial python API for brain.fm",
        long_description=README,
        classifiers=[
            "Development Status :: 2 - Pre-Alpha",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.5",
            "Topic :: Software Development :: Libraries"
        ],
        author="Joe Cross",
        author_email="joe.mcross@gmail.com",
        url="https://github.com/numberoverzero/brainfm",
        license="MIT",
        keywords="brainfm api",
        platforms="any",
        include_package_data=True,
        packages=find_packages(exclude=("tests", "docs")),
        install_requires=["requests==2.11.1"],
    )