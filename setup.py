from setuptools import find_packages, setup
from typing import List

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"
REPO_NAME = "YTWEBrenderer"
AUTHOR_NAME = "VinodKumarJodu"
SRC_REPO = "YTWEBrenderer"

REQUIREMENTS_FILE_NAME = "requirements_dev.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements() -> List[str]:
    """
    This Function will return the list of requirements listed in requirements.txt
    """
    requirements_list: List[str]= []
    with open(REQUIREMENTS_FILE_NAME,'r') as f:
        # contents = csv.reader(f)
        # requirements_list = [line[0] for line in contents]
        if HYPHEN_E_DOT in requirements_list:
            requirements_list.remove(HYPHEN_E_DOT)
        print(requirements_list)
    return requirements_list

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
    packages=find_packages(),
    install_requires = get_requirements()
)
