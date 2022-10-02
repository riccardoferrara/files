from setuptools import find_packages, setup
setup(
    name='files',
    packages=find_packages(include=['files']),
    version='0.2.0',
    description='some of the most common file functions (write file, write json, get dirs, ...)',
    author='riccardo85ferrara@gmail.com',
    license='MIT',
    install_requires=['setuptools==63.4.3','xlsx2csv==0.8.0']
)