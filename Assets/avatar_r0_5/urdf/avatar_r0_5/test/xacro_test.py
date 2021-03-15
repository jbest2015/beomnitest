#!/usr/bin/env python
import os
import unittest

import rospkg

from xacro import process_file


class TestXacro(unittest.TestCase):
    def test_single_xacro(self):
        r = rospkg.RosPack()
        process_file(os.path.join(r.get_path('avatar_r0_5'), 'urdf', 'avatar_r0_5.urdf.xacro'),
                     mappings={'use_nominal_extrinsics': 'true'})


if __name__ == '__main__':
    import rosunit
    rosunit.unitrun('avatar_base', 'test_xacro', TestXacro)
