from setuptools import setup, find_packages

# Read the contents of your README file for the long description
with open("README.md", "r") as fh:
    long_description = fh.read()

# Setup configuration
setup(
    name='spm-python',
    version='25.01-alpha2', 
    author='Johan Medrano',
    author_email='johan.medrano@ucl.ac.uk', 
    description='Python bindings for the SPM software.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/spm/spm-python',
    packages=find_packages(),  
    include_package_data=True, 
    package_data={
        'spm': ['_spm/_spm.ctf'], 
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GPL2', 
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'numpy',
        'scipy'
    ],
    python_requires='>=3.9,<=3.12',  
)
