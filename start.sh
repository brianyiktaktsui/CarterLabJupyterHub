#!/bin/sh
mkdir notebooks
cd notebooks
git init
git pull https://github.com/brianyiktaktsui/CarterLabJupyterHub.git

jupyter trust /home/jovyan/notebooks/*ipynb
