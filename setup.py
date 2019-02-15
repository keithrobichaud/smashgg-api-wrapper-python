import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smashggAPI",
    version="0.0.2",
    author="Keith Robichaud",
    author_email="keith@smash.gg",
    description="A wrapper for smash.gg's GraphQL API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/keithrobichaud/smashgg-api-wrapper-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)