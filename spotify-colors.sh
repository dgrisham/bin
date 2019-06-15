#!/bin/bash

while sleep 5; do
    new=$(spotify-now -i '%album')
    if [[ "$new" != "$old" ]]; then
        scc
    fi
    old="$new"
done
