from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name="json2latex",
    version="0.0.2",
    author="Cameron Devine",
    author_email="camdev@uw.edu",
    description="A package for converting JSON and other similar structures to a format accessible using LaTeX.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    scripts=["scripts/json2latex"],
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Markup :: LaTeX",
    ],
    install_requires=["roman"],
    url="https://github.com/CameronDevine/json2latex",
)
