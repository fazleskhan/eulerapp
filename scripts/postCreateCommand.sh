#!/bin/bash

echo "Executing ./scripts/postCreateCommand.sh"

# apt update is not working because the pub key has expired
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | gpg --dearmor | sudo tee /usr/share/keyrings/yarn.gpg >/dev/null

echo "deb [signed-by=/usr/share/keyrings/yarn.gpg] https://dl.yarnpkg.com/debian stable main" | sudo tee /etc/apt/sources.list.d/yarn.list

sudo apt update

sudo apt upgrade -y

sudo apt install python-is-python3

pip install -r requirements.txt
