from setuptools import find_packages, setup

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"
REPO_NAME = "YTWEBrenderer"
AUTHOR_NAME = "VinodKumarJodu"
SRC_REPO = "YTWEBrenderer"

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email="vinodkumarjodu@gmail.com",
    long_description=long_description,
    long_description_content="text/makdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)
