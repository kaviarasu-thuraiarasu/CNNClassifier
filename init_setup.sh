echo [$(date)]:"Start"
echo [$(date)]:"Creating Environment with python version 3.8"
python template.py
conda create --prefix ./env python=3.8 -y
echo [$(date)]:"Activating the Environment"
source activate ./env

echo [$(date)]:"Installing Dev Requirements"
pip install -r requirements_dev.txt
echo [$(date)]:"End"