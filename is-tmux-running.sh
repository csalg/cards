session="bg"

# Check if the session exists, discarding output
# We can check $? for the exit status (zero for success, non-zero for failure)
tmux has-session -t $session 2>/dev/null

if [ $? != 0 ]; then
  echo "Running"
  # Set up your session
fi

# Attach to created session
tmux attach-session -t $session
