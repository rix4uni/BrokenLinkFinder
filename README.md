# BrokenLinkFinder

A Light Weight Tool to find social media accounts.

## Installation
```
git clone https://github.com/rix4uni/BrokenLinkFinder.git
cd BrokenLinkFinder
pip3 install -r requirements.txt
```

## Example usages

Single URL:
```
echo "https://www.hackerone.com" | python3 brokenlinkfinder.py
```

Output
```
URL: https://www.hackerone.com
https://www.facebook.com/Hacker0x01
https://www.twitter.com/Hacker0x01
https://www.linkedin.com/company/hackerone
https://www.instagram.com/hacker0x01
```

Multiple URLs:
```
cat alive-subs.txt | python3 brokenlinkfinder.py
```

```
usage: brokenlinkfinder.py [-h] [-t THREADS] [--timeout TIMEOUT]

options:
  -h, --help            show this help message and exit
  -t THREADS, --threads THREADS
                        number of threads to use (default 50)
  --timeout TIMEOUT     timeout in seconds (default 5)
  ```
