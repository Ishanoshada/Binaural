# setup.py
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="binaural",
    version="0.1.2",
    author="ishan Oshada",
    author_email="ishan.kodithuwakku.offical@gmail.com",
    description="A Python package for generating binaural beats and brainwave entrainment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ishanoshada/binaural",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    install_requires=[
        "numpy",
        "scipy",
    ],
    keywords="binaural beats, brainwave entrainment, audio processing, sound synthesis",
)

