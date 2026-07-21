#!/bin/bash

echo "Starting mcp_server"

HOST=0.0.0.0 \
MCP_AUTO_OPEN_ENABLED=false \
DANGEROUSLY_OMIT_AUTH=true \
mcp dev mcp_server.py