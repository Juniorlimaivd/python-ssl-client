import setuptools

CLIENT_VERSION = "1.1.0"
PACKAGE_NAME = "sslclient"

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('LICENSE.txt', "r") as f:
    license = f.read()

EXTRAS = {}
REQUIRES = []

with open('requirements.txt') as f:
    for line in f:
        line, _, _ = line.partition('#')
        line = line.strip()
        if ';' in line:
            requirement, _, specifier = line.partition(';')
            for_specifier = EXTRAS.setdefault(':{}'.format(specifier), [])
            for_specifier.append(requirement)
        else:
            REQUIRES.append(line)

setuptools.setup(
    name="sslclient",
    version="1.1.0",
    author="Junior Lima",
    author_email="junior.lima.ivd.2@gmail.com",
    license=license,
    description="SSLVision client API in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/juniorlimaivd/python-ssl-vision",
    packages=setuptools.find_packages(exclude=('tests', 'examples')),
    install_requires=REQUIRES,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

