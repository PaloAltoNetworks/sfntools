from setuptools import setup

setup(
    name="sfntools",
    version='0.1',
    py_modules=['sfn_tools'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        sfntools=sfn_tools:cli
    ''',
)
