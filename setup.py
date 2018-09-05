from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tuimoji',
    version='1.0.0',
    description='A terminal ui based emoji selector.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Fingel/tuimoji',
    author='Austin Riba',
    author_email='austin@m51.io',
    license='GPLv3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: System :: Console Fonts',
        'Topic :: Text Processing :: Fonts',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
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
