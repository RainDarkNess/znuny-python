from setuptools import setup

setup(
    name='znuny-python',
    version='0.0.1',
    url='https://github.com/RainDarkNess/znuny-python.git',
    author='RainDarkNess',
    author_email='pooplolo52@gmail.com',
    description='A simple Python module for interfacing with the znuny.',
    package_dir={
        "": "src",
        "znuny": "src/znuny",
        "znuny.connector": "src/znuny/connector"
    },
    packages=['znuny', 'znuny.connector'],
    install_requires=[
        'requests >= 2.25.1',
        'keyring >= 23.0.1'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)