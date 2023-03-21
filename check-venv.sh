#!/bin/bash
INVENV=$( python3 -c 'import sys ; print( "" if sys.prefix == sys.base_prefix else 1 )' )
if [[ "$INVENV" == "" ]]
then
    echo "Not in a virtual environment, will not proceed with installation"
    echo "To install the testing environment:"
    echo "  1. Run 'make venv' to create a virtual environment"
    echo "  2. Run 'source ${HOME}/huntingtest/huntingtest/bin/activate' to activate virtual environment"
    exit 1
fi