#!/bin/bash
set -euo pipefail

echo "Executing ./scripts/postCreateCommand.sh"

# apt update is not working because the pub key has expired
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | gpg --dearmor | sudo tee /usr/share/keyrings/yarn.gpg >/dev/null

echo "deb [signed-by=/usr/share/keyrings/yarn.gpg] https://dl.yarnpkg.com/debian stable main" | sudo tee /etc/apt/sources.list.d/yarn.list

sudo apt update

sudo apt upgrade -y

sudo apt install python-is-python3

echo "Installing MCP Inspector..."

npm install --global @modelcontextprotocol/inspector

echo "Installed MCP Inspector package:"
npm list --global @modelcontextprotocol/inspector --depth=0

pip install -r requirements.txt

# prevent changes to the .env file from being commited to the repo
git update-index --skip-worktree .env

sudo install -d -m 0755 /etc/apt/keyrings

sudo curl -fsSL https://downloads.claude.ai/keys/claude-code.asc \
    -o /etc/apt/keyrings/claude-code.asc

echo "deb [signed-by=/etc/apt/keyrings/claude-code.asc] https://downloads.claude.ai/claude-code/apt/stable stable main" \
| sudo tee /etc/apt/sources.list.d/claude-code.list >/dev/null

sudo apt update

sudo apt install -y claude-code
