# https://setuptools.readthedocs.io/
import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()

requires = [
    "uvicorn==0.13.4",  # [standard]",
]
requires_web = [
    "fastapi",
    "starlette>=0.13.0,<0.14.0"
]

requires_db = [
    "gino-starlette==0.1.1",
    "gino==1.0.0",  # [starlette]",
    "asyncpg==0.22.0",
    "SQLAlchemy<1.4",
    "alembic==1.6.2",
    "psycopg2",
]

tests_require = [
    "pytest",
    "requests",
]

setup(
    name='web_fastapi',
    version='1.0',
    description='web_fastapi description',
    long_description=README,
    classifiers=[
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    python_requires='>3.6, !=3.6.2, !=3.7.*, <4',
    author='swdcgghxa',
    author_email='',
    url='https://github.com/swdcgghxa/web_fastapi',
    keywords='web fastapi',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    extras_require={
        'testing': tests_require,
        'db': requires_db,
        'web': requires_web,
    },
    entry_points={
        'web_fastapi.modules': [
            'a = web_fastapi.views',
            'b = web_fastapi.models',
        ],
        'console_scripts': [
            # '',
        ],
    },
)
