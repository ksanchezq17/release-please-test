from setuptools import setup, find_packages

setup(
    name="mypython",
    version="0.1",
    # packages=find_packages(where="src"),
    packages=['mypython', 'mypython.module'],
    package_dir={"": "src"}
)