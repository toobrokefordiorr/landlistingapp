from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in demo_app/__init__.py
from demo_app import __version__ as version

setup(
	name="demo_app",
	version=version,
	description="Demo App",
	author="Shawn",
	author_email="shawnndubisi0@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
