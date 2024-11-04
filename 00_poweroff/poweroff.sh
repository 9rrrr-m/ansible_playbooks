#!/bin/bash

WORKDIR=/home/ansible/ansible/00_poweroff
INVENTORY=$WORKDIR/inventory
> $INVENTORY

NET=192.168.10
for i in {11..14}
do
    ping -c1 -W1 $NET.$i >/dev/null 2>&1
    [ $? -eq 0 ] && echo $NET.$i >> $INVENTORY
done

cd $WORKDIR
if [ -s $INVENTORY ] ; then
    ansible-playbook $WORKDIR/targethost.yml 
    ansible-playbook $WORKDIR/controlhost.yml
else
    ansible-playbook $WORKDIR/controlhost.yml
fi
