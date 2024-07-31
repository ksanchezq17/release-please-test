from setuptools import setup

setup(
    name="mypython",
    version="0.1",
    # packages=find_packages(where="src"),
    packages=["mypython", "mypython.module"],
    package_dir={"": "src"},
)
