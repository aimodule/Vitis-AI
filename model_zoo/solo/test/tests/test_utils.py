# Copyright 2019 Xilinx Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy.testing as npt

from mmdet.utils.flops_counter import params_to_string


def test_params_to_string():
    npt.assert_equal(params_to_string(1e9), '1000.0 M')
    npt.assert_equal(params_to_string(2e5), '200.0 k')
    npt.assert_equal(params_to_string(3e-9), '3e-09')
