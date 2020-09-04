
#!/bin/bash

CONTAINER="instark"
REPOSITORY="https://github.com/knowark/instark.git"
PLAYBOOK="setup/local.sh"

echo "Deploying LXD container..."

lxc launch ubuntu:20.04 $CONTAINER
lxc config device add $CONTAINER home disk source=$HOME path=/mnt/home

echo "Install Git and Ansible..."

sleep 5  # Wait for container network connectivity.
lxc exec $CONTAINER -- apt update -y
lxc exec $CONTAINER -- apt install ansible -y
lxc exec $CONTAINER -- apt autoremove -y

echo "Deploy with Ansible Pull..."

# lxc exec $CONTAINER -- bash -c "ansible-pull --connection=local -i 127.0.0.1, \
#     -U $REPOSITORY -d /var/git/$CONTAINER $PLAYBOOK 2>&1 | tee deploy.log"
