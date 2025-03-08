''' 
The setup.py file is an essential part of packaging and distributing
python projects. It is used by setuptools to define the configuration
of your project, such as its metadata, dependencies, and more
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    '''
    this functions returns the list of requirements
    '''
    requirement_lst :List[str] = []
    try:
        with open('requirements.txt','r') as file:
            #read lines from the file
            lines = file.readlines()
            #process each line
            for line in lines:
                requirement = line.strip()
                # ifnore empty lines and -e.
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    
    except FileNotFoundError:
        print("requirements.txt file not found.")

    
    return requirement_lst

setup(

    name = 'networksecurity',
    version = '0.0.1',
    author = 'Sandeep preetham',
    authon_email ='msandeepreetham@gmal.com',
    packages = find_packages(),
    install_requires = get_requirements(),
    description = 'A network security project'
)
                    
