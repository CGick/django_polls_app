import os
from setuptools import find_packages, setup

with open(
        os.path.join(
            os.path.dirname(__file__),
            'README.rst'
        )) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(
    os.path.normpath(
        os.path.join(
            os.path.abspath(__file__),
            os.pardir
        )
    )
)

setup(
    name='django_polls',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='A simple Django app to conduct Web-based polls. Created in Django tutorial.',
    long_description=README,
    url='https://www.example.com/',
    author='Chris Gick',
    author_email='chrisgick31@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)
