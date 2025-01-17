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

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.
import os

from yolox.exp import ExpBallsQat as MyExp


class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 0.67
        self.width = 0.75
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]

        # Define yourself dataset path
        self.data_dir = "/workspace/model_zoo/yolox/datasets"
        self.train_ann = "train.json"
        self.val_ann = "val.json"

        self.num_classes = 3

        self.warmup_epochs = 5
        self.max_epoch = 10
        self.data_num_workers = 4
        self.is_qat = True
        self.float_ckpt = './YOLOX_outputs/yolox_m_balls_float/best_ckpt.pth'
        self.eval_interval = 10
        self.calib_dir = 'quantized'
