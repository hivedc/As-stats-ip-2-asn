# Convert ip2asn.tsv to ip2asn.json

Script that downloads data from [ip2asn](https://iptoasn.com/) and puts it into the right json format for [As-Stats](https://github.com/manuelkasper/AS-Stats)

Before the first start, verify requirements
Python has to be on version>= 3.0 
Command should be done from where the files were extracted
> **pip** install -r requirements.txt

Chmod to execute file
> **sudo chmod +x** ./ip_json_creator.py

Launch script
> **python3** ./ip_json_creator.py --name filename --of ./location

Backup your old asinfo.txt 
> **mv** asinfo.txt asinfo.txt.old


You may then copy this file to your As-stats folder
