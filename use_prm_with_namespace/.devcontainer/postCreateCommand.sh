sudo chown -R vscode:vscode /ros_ws

cd /ros_ws
rosdep update
rosdep install -i -y --from-path src

python3 -m pip install -U black pylint