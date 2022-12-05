# TensorFlow & PyTorch GPU Setup 


## Install PyTorch
Problem: recomended command install the cpu version   
``conda install pytorch-gpu==1.12.0 torchvision==0.13.0 torchaudio==0.12.0 cudatoolkit=11.2 -c pytorch -c conda-forge``

Work around: 
pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html

``pip install torch==1.9.0+cu11 torchvision==0.10.0+cu111 torchaudio==0.9.0+cu111 -f https://download.pytorch.org/whl/torch_stable.html``

#### Testing
``python3 -c "import torch; print(torch.cuda.is_available())"``

#### Resources
https://stackoverflow.com/questions/70653198/tensorflow-pytorch-install-cudatoolkit-11-2

Cuda 11.4 : compatable with 11.3 binaries  
https://github.com/pytorch/pytorch/issues/75992

Therefore
pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113

Now no matplotlib  


## Install TensorFlow

``conda activate tf
conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/
mkdir -p $CONDA_PREFIX/etc/conda/activate.d
echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/' > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
pip install --upgrade pip
pip install tensorflow``

### TF requirments: 

*  NVIDIA® GPU drivers version 450.80.02 or higher.
*  CUDA® Toolkit 11.2.
*  cuDNN SDK 8.1.0.
*  (Optional) TensorRT to improve latency and throughput for inference.

![image](https://user-images.githubusercontent.com/23053125/205438774-0d2c26ef-f011-402a-9bdd-acf8e5294d06.png)
https://docs.nvidia.com/deploy/cuda-compatibility/index.html

#### Resouces  
https://www.tensorflow.org/install/pip 

## CUDA Debugging
 
Problem :  
``nvidia-smi`` 

``Failed to initialize NVML: Driver/library version mismatch``

``cat /proc/driver/nvidia/version``  
NVRM version: NVIDIA UNIX x86_64 Kernel Module  470.141.03  Thu Jun 30 18:45:31 UTC 2022
GCC version:  gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.1)

#### Remove ALL NVIDEA: Clean Start

``sudo apt-get --purge remove "*nvidia*"``  
``sudo /usr/bin/nvidia-uninstall``

Then can check with
``lsmod | grep nvidia``

More Info:  

#### Current solution
Driver from Ubuntu Software and updates -> additional drivers (ignore TF for now)
NVIDIA driver metapackage-470 
Installed pytorch on clean env

``pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113``
then   
``conda install -c conda-forge albumentations``
Only this order will be solvable in conda
pytorch.yml is setup up

## RCNN Tutorial
They used PyTorch 1.10  
https://debuggercafe.com/a-simple-pipeline-to-train-pytorch-faster-rcnn-object-detection-model/

I plan on doing this gude and first swapping out the data with the prepaired one on Roboflow  ( and later our preprocessed one )  
https://public.roboflow.com/object-detection/brackish-underwater/2

Dependencies:
``conda install -c conda-forge albumentations``
Open CV (looks like its bundled with albumentations so need to test)

#### Current Problem
GLIBCXX_3.4.30' not found  
``conda install -c conda-forge gcc=12.1.0``  
https://stackoverflow.com/questions/72540359/glibcxx-3-4-30-not-found-for-librosa-in-conda-virtual-environment-after-tryin

See installed 
``strings /usr/lib/x86_64-linux-gnu/libstdc++.so.6 | grep GLIBCXX``  
https://askubuntu.com/questions/1418016/glibcxx-3-4-30-not-found-in-conda-environment

The package exists on the system however it is not linked into the conda enviroment  
``ln -sf /usr/lib/x86_64-linux-gnu/libstdc++.so.6 /home/melika/miniconda3/envs/pytorch/bin/../lib/libstdc++.so.6``   

``conda install -c conda-forge libstdcxx-ng=12``  
https://github.com/lhelontra/tensorflow-on-arm/issues/13#issuecomment-489296444

example needs matplotlib  
``conda install -c conda-forge matplotlib`` 

caused clash flex solve stops cxx fix again error   

``ImportError: /lib/x86_64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.30' not found (required by /home/melika/miniconda3/envs/pytorch/lib/python3.10/site-packages/scipy/fft/_pocketfft/pypocketfft.cpython-310-x86_64-linux-gnu.so)``
  
Tried forum suggestion  
''pip uninstall scikit-build'' 


## Conda Env Managment

#### env cloning 
``conda create --name copy_env --clone original``
#### env remove
``conda env remove -n pytorch``
#### env export
``conda env export > environment_droplet.yml``
#### env from yml
``conda env create -f environment.yml``

#### Dataspell 
Server setup
``ssh mk`` 
``conda activate pytorch``  
``jupyter notebook --no-browser --port=8887&``  
Local device  
``ssh -N -L localhost:8887:localhost:8887 mk``  
Add jupyter connection -> paste url with token attatched  
