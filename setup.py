from setuptools import setup


setup(
    name="pytreepy",
    author="Nathan Klapstein",
    author_email="nklapste@ualberta.ca",
    version="0.0.0",
    description="A python module for creating printable string represntations of directories",
    url="https://github.com/nklapste/pytreepy",
    download_url="https://github.com/nklapste/pytreepy/archive/1.4.tar.gz",
    packages=["pytreepy"],
    package_data={
        '': ['README.md'],
    },
    install_requires=[],
)
