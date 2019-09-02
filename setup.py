#!/usr/bin/env python

from setuptools import setup, find_packages
import io

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='twitterprofiling',
    version='0.2.5',
    description='This tool provides an easy way to generate a preferences profile of a given twitter user',
    packages=find_packages(),
    license='MIT License',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/bisite/TwitterProfiling',
    author='Juanju',
    author_email='juanjucm17@gmail.com',
    install_requires=['tweepy==3.7.0',
                      'pandas==0.24.2',
                      'numpy==1.16.2',
                      'scikit-learn==0.21.3',  # Needed to unpickle estimators
                      'gensim==3.8.0',
                      'spacy==2.1.8',
                      'en_core_web_sm @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.1.0/en_core_web_sm-2.1.0.tar.gz',
                      'flask', 'flask_cors', 'flask_restplus',  # Web server
                      ],
    keywords='profile, twitter, natural language processing, NLP, preferences,api',
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    data_files=[
           ('data/models/nmf', ['twitterprofiling/data/models/nmf/nmf.pickle', 'twitterprofiling/data/models/nmf/tfidf.pickle', 'twitterprofiling/data/models/nmf/tfidf_vectorizer.pickle'])
    ],
    include_package_data=True,
    entry_points={
            'console_scripts': [
                'twitterprofiling=twitterprofiling.server:main'
            ],
        },
)
