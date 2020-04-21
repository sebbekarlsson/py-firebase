from setuptools import setup, find_packages


setup(
    name='py_firebase',
    version='1.0.0',
    install_requires=[
        'pyrebase',
        'flask'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
        ]
    }
)
