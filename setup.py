from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()


VERSION = '0.1.7' 
DESCRIPTION = 'A python package used to perform quantum state tomography.'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="quantumstatetomo", 
        version=VERSION,
        author="Lana Bozanic",
        author_email="lbozanic@uottawa.ca",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        py_modules=['quantumstatetomo'],
        install_requires=['numpy', 'qutip', 'matplotlib', 'scipy'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python'],
        classifiers= [
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
        

)