from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: End Users/Desktop',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: Apache Software License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='zikasort',
  version='0.1',
  description='Timer for timing periods in school.',
  py_modules=["zimer"],
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  entry_points = {
      'console_scripts': ['zimer=zimer:main'],
  },  
  url='',  
  author='Zika Walter',
  author_email='example@example.com',
  license='APACHE', 
  classifiers=classifiers,
  keywords='sorter', 
  packages=find_packages(),
  install_requires=['']  
)
