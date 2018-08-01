import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="get_ipos",
    version="0.0.1",
    author="Sarthak Negi",
    author_email="sarthaknegi609@gmail.com",
    description="Get the IPOs listings from top exchanges",
    long_description_content_type="text/markdown",
    url="https://github.com/sarthaknegi/get_ipos",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    )
)