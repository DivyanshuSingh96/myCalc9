import setuptools

with open('README.md') as f:
    README = f.read()

setuptools.setup(
    name="myCalc9",
    version="v0.0.1",
    author="Divyanshu Singh",
    author_email="divyanshu.singh144400@gmail.com",
    license="MIT",
    description='A small mathematical library for quick calculations',
    long_description=README,
    url='',
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ]
)