#######################################################################
# This file is part of PyBlosxom.
#
# Copyright (C) 2010-2011 by the PyBlosxom team.  See AUTHORS.
#
# PyBlosxom is distributed under the MIT license.  See the file
# LICENSE for distribution details.
#######################################################################

import time
import os

from Pyblosxom.tests import PluginTest, TIMESTAMP
from Pyblosxom.plugins.archives import yeararchives

class Test_yeararchives(PluginTest):
    def setUp(self):
        PluginTest.setUp(self, yeararchives)

    def tearDown(self):
        PluginTest.tearDown(self)

    def test_parse_path_info(self):
        for testin, testout in [
            ("", None),
            ("/", None),
            ("/2003", ("2003", None)),
            ("/2003/", ("2003", None)),
            ("/2003/index", ("2003", None)),
            ("/2003/index.flav", ("2003", "flav")),
            ]:
 
            self.assertEquals(yeararchives.parse_path_info(testin),
                              testout)
