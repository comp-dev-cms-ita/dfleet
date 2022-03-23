import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dfleet",
    version="0.0.2",
    author="dciangot",
    author_email="diego.ciangottini@gmail.com",
    description="dfleet CLI to manage remote dask cluster",
    long_description=long_description,
    url="https://github.com/comp-dev-cms-ita/dfleet",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache2 License",
        "Operating System :: OS Independent",
    ],
    python_requires="~=3.6",
    license="MIT",
    scripts=['bin/dfleet'],
    install_requires=[
    'typer',
    'requests'
   ]
)