echo "Starting install..."
TARGET_DIR="$HOME/api/server_app"
SOURCE_CODE="https://github.com/Sreyas-108/server_app"
echo "Checking for system updates.."
sudo apt-get update
echo "Installing packages.."
sudo apt-get install python3.6
sudo apt-get install python3-venv
sudo apt-get install git-core
git clone $SOURCE_CODE $TARGET_DIR
cd "$TARGET_DIR"
python3 -m venv venv
source venv/bin/activate
echo "Installing requirements.."
pip install -r requirements.txt
echo "Setting permissions.."
sudo iptables -P INPUT ACCEPT
sudo iptables -P FORWARD ACCEPT
sudp iptables -P OUTPUT ACCEPT
echo "Server application installation complete.."
echo "Installed location is $TARGET_DIR"
echo "Proceed with starting the server application."