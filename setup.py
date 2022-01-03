import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="openapi-data-generator",
    version="1.0.0",
    author="Elyashiv Danino && RAZALKALY",
    author_email="elyashiv3839@gmail.com",
    description="Resolve schema and deploy to single schema",
    long_description="file: README.md",
    long_description_content_type="text/markdown",
    url="https://github.com/elyashiv3839/openapi-data-generator.git",
    download_url="https://github.com/elyashiv3839/openapi-data-generator/archive/refs/tags/1.0.0.tar.gz",
    project_urls={"Bug Tracker": "https://github.com/elyashiv3839/openapi-data-generator.git/issues"},
    classifier=[
        "Programming Language :: Python :: 3",
        "Licence :: RAFAEL",
        "Operating System :: Multi-platform",
    ],
    packages=['openapi_schema_generator'],
    python_requires=">=3.6",
    install_requires=["openapi-schema-generator==1.0.0", "rstr==3.0.0", "filelock==3.4.2"]
)
