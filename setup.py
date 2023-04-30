from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

des = 'PyScraping is a universal web-scraping util for'
dess = 'Python, built with simplicity in mind.'

setup(
    name='pyscraping',
    version='1.0.1',
    description= des + ' ' + dess,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Rio Agung Purnomo',
    author_email='rioagungpurnomo.ak@gmail.com',
    url='https://github.com/rioagungpurnomo/pyscraping',
    packages=['pyscraping'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.6',
    install_requires=[
      "requests",
      "bs4"
    ],
)
