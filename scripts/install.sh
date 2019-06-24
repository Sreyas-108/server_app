echo "Starting install..."
TARGET_DIR="$HOME/api"
SOURCE_CODE="https://github.com/LiquidGalaxyLab/liquid-galaxy-api"
sudo apt-get update
sudo apt-get install python3.6
sudo apt-get install python3-venv
sudo apt-get install git-core
git clone $SOURCE_CODE $TARGET_DIR
cd "$TARGET_DIR"
python3 -m venv venv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
