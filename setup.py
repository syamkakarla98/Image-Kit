from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='Image-Kit',
    url='https://github.com/syamkakarla98/Image-Kit',
    author='Syam Kakarla',
    author_email='Syamkakarla98@gmail.com',
    packages=['ImageKit'],
    install_requires=['numpy', 'matplotlib', 'Pillow', 'scipy'],
    version='0.1.0',
    license='MIT',
    description='A module for basic image processing.',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    python_requires=">=3.5.3",
    classifiers=["Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",] ,
)
