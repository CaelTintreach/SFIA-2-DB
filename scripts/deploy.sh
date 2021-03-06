#!/bin/bash
pwd
ls
echo "scp docker-compose.yaml node-1:/home/jenkins/docker-compose.yaml"

ssh node-1 << EOF
git clone https://github.com/CaelTintreach/SFIA-2-DB.git
git pull https://github.com/CaelTintreach/SFIA-2-DB.git
EOF

ssh node-1 << EOF
pwd
whoami
export DATABASE_URI=$DATABASE_URI
echo \$DATABASE_URI
export MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD
git clone https://github.com/CaelTintreach/SFIA-2-DB.git
git pull https://github.com/CaelTintreach/SFIA-2-DB.git
cd SFIA-2-DB
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
rm -r SFIA-2-DB
#sudo docker service scale stacktest_lgen=3
sudo docker stack services stacktest
ls
EOF

echo $DATABASE_URI