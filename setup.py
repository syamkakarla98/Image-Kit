from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Image-Kit',
    url='https://github.com/syamkakarla98/Image-Kit',
    author='Syam Kakarla',
    author_email='Syamkakarla98@gmail.com',
    # Needed to actually package something
    packages=['ImageKit'],
    # Needed for dependencies
    install_requires=['numpy', 'matplotlib', 'Pillow', 'scipy'],
    # *strongly* suggested for sharing
    version='1.0.0',
    # The license can be anything you like
    license='MIT',
    description='A module for basic image processing.',
    long_description=open('README.md').read(),
)
