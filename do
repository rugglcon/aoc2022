#!/usr/bin/env bash

case $1 in
    run)
        python3 "day$2"
        ;;
    make)
        mkdir "day$2"
        cp .main.template "day$2/__main__.py"
        touch "day$2/input.txt"
        touch "day$2/test.txt"
        ;;
esac
