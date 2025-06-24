from setuptools import setup, find_packages

setup(
    name="set-all-seeds",
    version="0.1.0",
    description="Set all random seeds for reproducibility in Python, NumPy, and TensorFlow.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "tensorflow"
    ],
    python_requires=">=3.7",
    url="https://github.com/yourusername/set-all-seeds",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
