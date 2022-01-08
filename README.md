# Megacut ✂️
A new powerful Python3 tool for managing internet on a local network
## Installation
```bash
git clone https://github.com/stryker-project/megacut
cd megacut
pip install -r requirements.txt
python3 megacut.py
```
## Options & Syntax
python3 megacut.py target gateway -m\\-k\\-b\\-r

   -k Kill inet on target ip
   
   -m Permanently disable inet on target (only if -k not works)
   
   -b Disable inet for 20 seconds
   
   -r Restore inet on target ip
   

## Examples:

`python3 megacut.py 192.168.1.101 192.168.1.1 -k`
