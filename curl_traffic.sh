#!/bin/bash

timeout 120 while true; do curl localhost; sleep $((RANDOM % 4)); done
