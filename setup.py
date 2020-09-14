import setuptools

setuptools.setup(
    name='estore-client',
    version='0.0.1',
    description='Event Store Client',
    author='Jnxy',
    author_email='jnxy@lostwire.net',
    license='BSD',
    zip_safe=False,
    include_package_data=True,
    install_requires = [
        'asyncio',
        'aiohttp',
        'aiohttp-session',
        'estore-base',
    ],
    packages=setuptools.find_napespace_packages(include=['estore.*']))
