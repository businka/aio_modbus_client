import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aio_modbus_client",
    version="0.0.1",
    author="Mikhail Razgovorov",
    author_email="author@example.com",
    description="Easy work with modbus device. You do not need to know the protocol.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/businka/aio_modbus_client",
    packages=setuptools.find_packages(),
    python_requires='>=3.5.3',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: OS Independent",
    ],
)