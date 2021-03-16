import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyslack",
    version="1.0.2",
    author="Michael Kerry",
    author_email="michael_kerry@harvard.edu",
    description="A package to facilitate the use of slack webhook for notifications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/huit/pyslack",
    project_urls={
        "Bug Tracker": "https://github.com/huit/pyslack/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'requests==2.25.1',
      ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)