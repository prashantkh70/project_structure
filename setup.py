# to build this application and use it as packaage

from setuptools import find_packages,setup
from typing import List

HYPER_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    """ This function will retuen the list of requirements
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements]

        if HYPER_E_DOT in requirements:
            requirements.remove(HYPER_E_DOT)
    return requirements

setup(
name="project_structure", 
version= "0.0.1",
author= "Prashant",
author_email="prashantkh7000@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
# install_requires=["pandas","numpy","seaborn"]

)