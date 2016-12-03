from distutils.core import setup

setup(
    name = 'EasySqrt',
    version = '0.1.0',
    description = 'The easiset way to find a numbers Sqrt',
    author = 'GrgBls',
    author_email = 'gmpalis6@gmail.com',
    url = 'https://github.com/GrgBls/EasySqrt', 
    py_modules=['EasySqrt'],
    install_requires=[
        # list of this package dependencies
    ],
    entry_points='''
        [console_scripts]
        EasySqrt=EasySqrt:cli
    ''',
)
