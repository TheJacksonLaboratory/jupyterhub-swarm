#!/bin/bash
PASSWORD=pass
NUMBER_OF_USERS=2
for n in `seq -f "%02g" 1 $NUMBER_OF_USERS`
do
    echo creating user training$n
    echo training$n:$PASSWORD::::/home/training$n:/bin/bash | sudo newusers
done
