#!/bin/bash

timeout 120 bash -c 'while true; do curl -k https://google.com; sleep $((RANDOM % 4)); done'
