from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name="blockscout-python",
    version="0.1.1",
    description="Python API for blockscout.com explorers",
    long_description=long_description,
    long_description_content_type="text/markdown",    
    url="https://github.com/defipy-devs",
    author="icmoore",
    author_email="defipy.devs@gmail.com",
    license="MIT",
    package_dir = {"blockscout": "python/prod"},
    packages=[
        "blockscout",
        "blockscout.explorer",
        "blockscout.cull",
        "blockscout.configs",
        "blockscout.enums",
        "blockscout.modules",
        "blockscout.utils",
    ],
    install_requires=["requests"],
    include_package_data=True,
    zip_safe=False,
)
