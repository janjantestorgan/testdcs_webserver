from setuptools import setup, find_packages

setup(
    name="web_server",
    version="1.0.0",
    packages=find_packages(exclude=("unittests",)),
    # packages=find_packages(),
    # include_package_data=True,
    # python_requires=">=3.8",
    # install_requires=[
    #    "paho-mqtt",
    #    "pyserial",
    # ],
)
