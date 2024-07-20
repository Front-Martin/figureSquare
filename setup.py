import setuptools

from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='figuresquare',
  version='0.0.1',
  author='front_martin',
  author_email='martynenko3131@gmail.com',
  description='Module for calculating square of figures.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/Front-Martin/figureSquare',
  packages=find_packages(),
  classifiers=[
    'Programming Language :: Python :: 3.12'
  ],
  keywords='figures triangle circle square',
  project_urls={
    'GitHub': 'https://github.com/Front-Martin/figureSquare'
  },
  python_requires='>=3.6'
)