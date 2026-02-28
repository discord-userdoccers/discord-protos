from setuptools import setup, find_packages
import re

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('discord_protos/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

with open('README.md') as f:
    readme = f.read()

setup(
    name='discord-protos',
    author='Dolfies',
    url='https://github.com/dolfies/discord-protos',
    project_urls={
        'Issue tracker': 'https://github.com/dolfies/discord-protos/issues',
    },
    version=version,
    packages=['discord_protos', *find_packages()],
    license='MIT',
    description='Discord user settings protobufs.',
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=requirements,
    python_requires='>=3.8.0',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
