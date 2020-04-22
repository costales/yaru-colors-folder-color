#!/usr/bin/env python3

# Copyright (C) 2020 Jan Schroder https://github.com/Jannomag/Yaru-Colors
# Copyright (C) 2020 Jan Schroder https://github.com/costales/yaru-colors_and_folder-color/
#
# This software is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; if not, see http://www.gnu.org/licenses 
# for more information.


import os, sys, DistUtilsExtra.auto

# Create data files
#data = [ ('/usr/share/icons/Yaru', glob.glob('icons/*'))]

# Setup stage
DistUtilsExtra.auto.setup(
    name         = "yaru-colors_and_folder-color",
    version      = "0.0.1",
    description  = "Adap Yaru-Colors for working with Folder Color in Ubuntu 20.04",
    author       = "Marcos Alvarez Costales https://costales.github.io/",
    author_email = "marcos.costales@gmail.com",
    url          = "https://github.com/costales/yaru-colors_and_folder-color",
    license      = "GPL3"#,
    #data_files   = data
    )

