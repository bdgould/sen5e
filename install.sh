#!/usr/bin/env bash

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

printf "${YELLOW}######## Installing required packages...${NC}\n"
#sudo apt-get install python3 python3-pip

printf "${YELLOW}######## Running pip install...${NC}\n"
#pip3 install -r $(dirname $0)/requirements.txt

ME=$( whoami )
BASE=$( dirname `readlink -f $0` )
LINK_TO="/usr/local/bin/sen5e"
CONF_DIR="/etc/sen5e"
SERVICE_UNIT="/lib/systemd/system/sen5e.service"



printf "${YELLOW}######## Making dirs and symlinks...${NC}\n"
sudo unlink ${LINK_TO}
sudo ln -s ${BASE}/sen5e/sen5e ${LINK_TO}
sudo cp ${BASE}/sen5e.service
sudo chmod 644 ${SERVICE_UNIT}
sudo mkdir -p ${CONF_DIR}
sudo chown ${ME}:${ME} ${CONF_DIR}
cp ${BASE}/config.json ${CONF_DIR}/config.json


printf "${RED}######## Configure your /etc/sen5e/config.json...${NC}\n"

