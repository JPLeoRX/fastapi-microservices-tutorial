from setuptools import setup, find_packages


with open("README.md", "r") as readme_file:
    readme_text = readme_file.read()


setup_args = dict(
    name='library-utils',
    version='0.1',
    description='',
    keywords=[],
    long_description=readme_text,
    long_description_content_type="text/markdown",
    license="",
    packages=find_packages(),
    author="",
    author_email="",
)


install_requires = [
    'injectable',
]


if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
