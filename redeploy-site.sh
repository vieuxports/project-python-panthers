#!/bin/bash
pkill -f tmux 

cd project-python-panthers

/usr/bin/git fetch && /usr/bin/git reset origin/main --hard

source python3-virtualenv/bin/activate

pip install -r requirements.txt

tmux new-session -d "source python3-virtualenv/bin/activate && flask run --host=0.0.0.0"
