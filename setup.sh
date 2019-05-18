#! /bin/bash

apt-get update && \
apt-get -y install --install-recommends --fix-missing $(cat apt-requirements.txt)

echo "Installed all apt requirements"