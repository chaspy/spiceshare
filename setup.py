from setuptools import setup,find_packages

setup(
        name='spiceshare',
        version='0.0.1',
        description='Japanese Curry spices share service',
        author='Kota Natsume',
        author_email='kota99949@gmail.com',
        url='https://gitlab.com/kota99949',
        license='BSD-3-Clause',
        packages=find_packages(exclude=('tests')),
        install_requires=['flask','Flask-RESTful','pymongo'],
        setup_requires=['pytest-runner'],
        tests_requires=['pytest', 'pytest-cov']
        )
