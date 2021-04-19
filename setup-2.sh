#!/bin/bash 

tar -xvzf mpmath-1.1.0.tar.gz
cd mpmath-1.1.0
sudo python3 setup.py install
cd ..
tar -xvzf aiger-1.9.9.tar.gz
cd aiger-1.9.9
./configure.sh && make
cp aigtoaig ../.
cd ..
sudo apt-get install libtinfo-dev
sudo dpkg -i libreadline-dev_8.0-4_amd64.deb
unzip abc-master.zip
cd abc-master
make
cp abc ../.
cd ..
sudo apt install python3-pip
sudo apt-get install libgmp-dev
sudo apt-get install libmpfr-dev
sudo apt-get install libmpc-dev
pip3 install gmpy2
