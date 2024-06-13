echo [$(date)]: "START"


echo [$(date)]: "creating environment with python 3.10.14 version" 


conda create -n venv python=3.10.14 -y


echo [$(date)]: "activating the environment" 

source activate venv

echo [$(date)]: "installing the dev requirements" 

pip install -r requirements.txt

echo [$(date)]: "END" 