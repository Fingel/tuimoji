from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tuimoji',
    version='0.0.1',
    description='A terminal ui based emoji selector.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Fingel/tuimoji',
    author='Austin Riba',
    author_email='austin@m51.io',
    license='GPLv3',
    classifiers=[
        'Classifier: Development Status :: 4 - Beta',
        'Classifier: Environment :: Console (Text Based)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'RequiresDist: xclip'
    ],
    keywords='emoji emojis console terminal',
    project_urls={
        'Documentation': 'https://github.com/Fingel/tuimoji',
        'Issues': 'https://github.com/Fingel/tuimoji/issues'
    },
    packages=find_packages(),
    install_requires=['urwid'],
    python_requires='>=3',
    package_data={
        'tuimoji': ['emojis.json']
    },
    entry_points={
        'console_scripts': [
            'tuimoji=tuimoji.tuimoji:main'
        ]
    }
)
