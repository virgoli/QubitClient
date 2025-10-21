# -*- coding: utf-8 -*-
# Copyright (c) 2025 yaqiang.sun.
# This source code is licensed under the license found in the LICENSE file
# in the root directory of this source tree.
#########################################################################
# Author: yaqiangsun
# Created Time: 2025/04/11 17:58:29
########################################################################

import os
import numpy as np
import cv2


def load_npz_file(file_path):
    with np.load(file_path, allow_pickle=True) as data:
        content = dict(data)
    return content