# YoloX
### Contents
1. [Installation](#installation)
2. [Preparation](#preparation)
3. [Eval/Test](#eval/test)
4. [Performance](#performance)
5. [Model_info](#model_info)

### Installation
1. Environment requirement
    - pytorch, opencv, more details seen in requirements.txt
    - vai_q_pytorch(Optional, required by quantization)
    - XIR Python frontend (Optional, required by quantization)

2. Installation with Docker

   - Please refer to [vitis-ai](https://github.com/Xilinx/Vitis-AI/tree/master/) for how to obtain the docker image.

   - Activate pytorch virtual envrionment in docker:
   ```shell
   conda activate vitis-ai-pytorch
   ```
   - Install all the python dependencies using pip:
   ```shell
   pip install --user -r requirements.txt
   ```
   - Compile the yolox using pip:
   ```shell
   python3 setup.py develop
   ```

### Preparation

Prepare Dataset diretory structure (COCO Dataset)
   ```
   + yolox/datasets/
      + train_img
      + val_img
      + train_anno.json
      + val_anno.json
   ```

### Eval/Test

1. Training 

    ```shell
    bash run_train.sh 
    ```
2. Demo
    ```shell
    bash run_demo.sh
    ```
3. Quantization
    ```shell
    bash run_quant_PTQ.sh
    ```
4. QAT Training(quantizing model directly would lead large accuracy drop, so we provide quantization training scripts to improve quantization accuracy.)
   ```shell
   bash run_quant_QAT.sh 
   ```    
6. QAT Testing and Dump xmodel
   ```shell
   bash run_qat_convert.sh 
   ```    
7. Compiling for target architecture
   ```shell
   bash run_compile.sh 
   ```    

### Model_info

1. Data preprocess
  ```
  data channel order: RGB(0~255)                  
  input size: h * w = 640 * 640
  mean = (0.0, 0.0, 0.0)
  std = (1.0, 1.0, 1.0)
  input = (input * normalize  - mean) / std
  ```
