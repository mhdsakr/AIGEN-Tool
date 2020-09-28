#!/bin/bash 

tar -xvzf mpmath-1.1.0.tar.gz
cd mpmath-1.1.0
sudo python setup.py install
cd ..
tar -xvzf aiger-1.9.9.tar.gz
cd aiger-1.9.9
./configure.sh && make
cp aigtoaig ../.
cd ..
sudo apt-get install libtinfo-dev
sudo dpkg -i libreadline-dev_7.0-3_amd64.deb
unzip abc-master.zip
cd abc-master
make
cp abc ../.
cd ..
sudo apt install python-pip
sudo apt-get install libgmp-dev
sudo apt-get install libmpfr-dev
sudo apt-get install libmpc-dev
pip install gmpy2
