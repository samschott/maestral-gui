# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name="maestral-gui",
    version="0.1",
    description="Open-source Dropbox client for macOS and Linux.",
    url="https://github.com/SamSchott/maestral-gui",
    author="Sam Schott",
    author_email="ss2151@cam.ac.uk",
    license="MIT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.6",
    setup_requires=["wheel"],
    install_requires=[
        'maestral-qt>=1.2.1;sys_platform=="linux"',
        'maestral-cocoa>=1.2.1;sys_platform=="darwin"',
    ],
    zip_safe=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
