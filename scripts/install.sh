echo "Starting install..."
TARGET_DIR="$HOME/api/server_app"
<<<<<<< HEAD
SOURCE_CODE="https://github.com/LiquidGalaxyLab/liquid-galaxy-api"
=======
SOURCE_CODE="https://github.com/Sreyas-108/server_app"
>>>>>>> 2e79be8a64b9f18ca2230cfac31496aa68110f9b
sudo apt-get update
sudo apt-get install python3.6
sudo apt-get install python3-venv
sudo apt-get install git-core
git clone $SOURCE_CODE $TARGET_DIR
cd "$TARGET_DIR"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
