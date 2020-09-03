from setuptools import setup, find_packages

setup(name='estore-client',
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
    ],
    packages=find_packages())
