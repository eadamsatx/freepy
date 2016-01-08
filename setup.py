# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# Iskren Hadzhinedev

from setuptools import setup, find_packages

setup(
    name = "freepy",
    version = "2.0.0",
    packages = find_packages('src'),
    package_dir = { '':'src' },
    install_requires=[ 'jinja2 == 2.8', 'llist == 0.4',
                       'pykka == 1.2.1', 'twisted == 15.5.0' ],
    include_package_data = True,
    author = "Thomas Quintana",
    author_email = "quintana.thomas@gmail.com",
    license = "Apache License 2.0",
    url = "https://github.com/thomasquintana/freepy",
    entry_points = {
        'console_scripts': [
          'freepy-server = freepy.run:main',
        ]
    }
)

