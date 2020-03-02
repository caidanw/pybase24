import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pybase24',
    version='1.0.0',
    author='Caidan Williams',
    author_email='caidanstevenwilliams@gmail.com',
    description='Encoder and decoder for the Base24 encoding.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mildmelon/pybase24',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
