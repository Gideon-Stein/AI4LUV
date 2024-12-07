conda create --name ai4luv_operational python=3.12
git clone https://github.com/facefusion/facefusion
cd facefusion
python install.py --onnxruntime default
conda install conda-forge::libstdcxx-ng

