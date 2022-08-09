#!/bin/sh
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space

sudo dpkg --add-architecture i386
sudo apt-get update
sudo apt-get install -y libseccomp-dev libseccomp-dev:i386

