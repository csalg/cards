cd /app
tmux new-session -s app -n "monitor" -d "python3 monitor.py"
tmux new-window -t "app:1" -n "flask" "python3 -m flask run --host=0.0.0.0"