import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CATS Twitter Mining Server",
    version="0.0.1",
    author="Janet van Bilsen",
    author_email="janet.vanbilsen@outlook.com",
    description="Software to use Raspberry Pi as Twitter mining server",
    long_description=""""CATS is a program that can be installed on a Raspberry Pi to turn it into a cost-effective Twitter mining server""",
    long_description_content_type="markdown",
    url="https://github.com/janetvanbilsen/Twitter-Mining-Raspberry_Pi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='=3.7',
)
