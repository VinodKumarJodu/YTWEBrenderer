echo [$(date)]: "Start"
echo [$(date)]: "Creating Conda Environment with python 3.8"
conda create --prefix ./venv python=3.8 -y
echo [$(date)]: "Activating the Created Environment"
source activate ./venv
echo [$(date)]: "Installing dev requirements"
pip install -r requirements.txt
echo [$(date)]: "End"
