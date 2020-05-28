cd /home/pi/Sylva/Pz/HomePage
mkdir log
sudo chmod 777 log
sudo python3 manage.py runsslserver 192.168.219.102:443 --certificate django.cert --key django.key
