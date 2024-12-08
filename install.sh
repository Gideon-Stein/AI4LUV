conda create --name ai4luv_operational python=3.12
git clone https://github.com/facefusion/facefusion
cd facefusion
python install.py --onnxruntime default

sudo apt --fix-broken install
sudo apt-get install portaudio19-dev
conda install portaudio
conda install conda-forge::libstdcxx-ng

conda install conda-forge::pygame 
pip install -r requirements.txt
