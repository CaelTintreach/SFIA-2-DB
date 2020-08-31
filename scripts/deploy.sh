#!/bin/bash
pwd
ls

ssh node-1 << EOF
git clone https://github.com/CaelTintreach/SFIA-2-Repair.git
EOF
ssh node-2 << EOF
git clone https://github.com/CaelTintreach/SFIA-2-Repair.git
EOF

ssh node-1 << EOF
pwd
whoami
export DATABASE_URI="$DATABASE_URI"
export MYSQL_ROOT_PASSWORD="$MYSQL_ROOT_PASSWORD"
git clone https://github.com/CaelTintreach/SFIA-2-Repair.git
cd SFIA-2-Repair
sudo docker pull caeltintreach/lgen:latest
sudo docker pull caeltintreach/ui:latest
sudo docker pull caeltintreach/ngen:latest
sudo docker pull caeltintreach/pgen:latest
sudo docker pull nginx
sudo docker stack deploy --compose-file docker-compose.yaml stacktest
sudo docker images
sudo docker container ls -a
sudo docker stack services stacktest
cd ..
rm -r SFIA-2-Repair
#sudo docker service scale stacktest_lgen=3
sudo docker stack services stacktest
ls
EOF