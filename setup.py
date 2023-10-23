from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='slardar',
    version='0.0.1',
    packages=find_packages(include=['slardar']),
    package_data={
        'slardar': ['py.typed'],
    },
    python_requires='>=3.10',

    url='https://github.com/lexdene/slardar',
    description='execution scheduler for asyncio',
    long_description_content_type='text/markdown',
    long_description=long_description,
)
