from setuptools import setup, find_packages

setup(
    name='fee_simulator',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click==7.1.1',
        'ortools==7.5.7466',
        'matplotlib==3.2.1',
        'numpy==1.22.0',
    ],
    entry_points='''
        [console_scripts]
        feesim=fee_simulator.cli:run
    ''',
)
