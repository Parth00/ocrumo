from setuptools import setup, find_packages
 
setup(name='lrucache',
      version='0.1',
      url='https://github.com/Parth00/ormuco/tree/master/Q3',
      author='Parth Dubal',
      author_email='dubalparth@gmail.com',
      description='',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)