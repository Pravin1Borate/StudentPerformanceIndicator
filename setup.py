from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open('requirements.txt') as fo:
        requirements = fo.readlines()
        requirements = [req.replace("\n","") for req in requirements]  #the requirement.txt fill will add \n in the file so to remove it we need to replace it with blank

        if HYPEN_E_DOT in requirements:
            """Used to remove -e . from requirements.txt which invokes the setup method"""
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Pravin Borate',
    author_email='1pravin.borate@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)