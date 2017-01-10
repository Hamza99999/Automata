#!/bin/sh

sudo pip install -r requirements.txt
git clone http://people.csail.mit.edu/hubert/git/pyaudio.git
sudo python pyaudio/setup.py install
sudo apt-get installl libportaudio-dev
sudo apt-get install python-dev
sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
python -m nltk.downloader punkt