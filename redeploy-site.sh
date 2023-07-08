#!/bin/bash

tmux kill-server
cd ~/mlh-portfolio
git fetch && git reset origin/main --hard
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt
tmux new -d "cd ~/mlh-portfolio && source python3-virtualenv/bin/activate && export FLASK_ENV=development && flask run --host=0.0.0.0"

