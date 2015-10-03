from __future__ import absolute_import

from setuptools import setup, find_packages

from version import cgcloud_version

setup(
    name='cgcloud-mesos',
    version=cgcloud_version,

    author='Christopher Ketchum',
    author_email='cketchum@ucsc.edu',
    url='https://github.com/BD2KGenomics/cgcloud',
    description='Setup and manage a Apache Mesos cluster in EC2',

    package_dir={ '': 'src' },
    packages=find_packages( 'src' ),
    namespace_packages=[ 'cgcloud' ],
    install_requires=[
        'cgcloud-lib==' + cgcloud_version,
        'cgcloud-core==' + cgcloud_version,
        'bd2k-python-lib==1.8.dev1',
        'Fabric>=1.7.0',
        'lxml>=3.2.1' ] )