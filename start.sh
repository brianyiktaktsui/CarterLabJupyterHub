#!/bin/sh
gitpuller https://github.com/brianyiktaktsui/CarterLabJupyterHub master notebooks 
jupyter trust /home/jovyan/notebooks/*ipynb