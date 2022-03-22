#!/bin/bash

DOWNLOAD_PATH=$HOME/.opt
VENV_PATH=$HOME/.venv
VENV_ENV=torch_latest

mkdir -p $DOWNLOAD_PATH
cd $DOWNLOAD_PATH
echo "Activating venv environment"
source $VENV_PATH/$VENV_ENV/bin/activate

pip list | grep cython >/dev/null
if [ $? = 1 ]; then
  pip install cython
fi

git clone https://github.com/cocodataset/cocoapi.git
cd cocoapi/PythonAPI
make && make install
