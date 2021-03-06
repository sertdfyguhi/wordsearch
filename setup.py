import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="word-searcher",
    version="1.0.0",
    author="hdwyx",
    description="Package for searching words",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hdwyx/word-searcher",
    project_urls={
        "Bug Tracker": "https://github.com/hdwyx/word-searcher/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=2.7",
)