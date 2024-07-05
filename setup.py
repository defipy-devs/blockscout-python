from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(name='blockscout-python',
      version='0.0.1',
      description='blockscout-python',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://github.com/icmoore/defipi',
      author = "icmoore",
      author_email = "defipy.devs@gmail.com",
      license='MIT',
      package_dir = {"blockscout-python": "python/prod"},
      packages=[
          'blockscout-python',
          'blockscout-python.erc'
      ],   
      zip_safe=False)
