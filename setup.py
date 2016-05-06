#!/usr/bin/python
# Copyright (c) 2012 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

name = 'idarea'


setup(
    name=name,
    version='1.1',
    description='cloud console',
    license='xx',
    author='sss',
    author_email='zhu__feng014@163.com',
    url='https://org/',
    packages=find_packages(exclude=['test', 'bin']),
    test_suite='nose.collector',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.6',
        'Environment :: No Input/Output (Daemon)',
        ],
    install_requires=[], 
#    scripts=[
#        'bin/cloud-web-server',
#        'bin/cloud-monitor-server',
#        'bin/cloud-config-executor',
#    ],
    entry_points={
        'paste.app_factory': [
            'object = idarea.object.server:app_factory',
            ],
        },
    )
