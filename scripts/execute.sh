cd $HOME/api/server_app
source venv/bin/activate
echo "Updating requirements.."
pip install -r requirements.txt
echo "Setting permissions.."
sudo iptables -P INPUT ACCEPT
sudo iptables -P FORWARD ACCEPT
sudp iptables -P OUTPUT ACCEPT
python -m app