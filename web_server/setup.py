from setuptools import setup, find_packages

setup(
    name="web_server",
    version="1.0.0",
    packages=find_packages(exclude=("unitests",)),
    install_requires=[
        'paho-mqtt',
        'pyserial',
    ],
)
