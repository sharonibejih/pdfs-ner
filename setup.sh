#!/bin/sh

sudo apt update

python -m pip install -–upgrade pip
pip install -r requirements.txt

apt-get update && apt-get install -y python3-opencv

sudo apt install tesseract-ocr -y
apt-get install poppler-utils
