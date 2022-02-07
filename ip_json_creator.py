import json
import requests
import gzip
import ipaddress
import os
import parser

# Indicates response status code
OK = 200
# Url of file/archive to download
URL = 'https://iptoasn.com/data/ip2asn-combined.tsv.gz'
#Name of downloaded archive
ARCHIVE_NAME = "ip2asn-combined.tsv.gz"

class IpJsonCreator:
    def __init__(self, Parser):
        #retrieves name and destination path from CLI arguments
        self.output_file_name = Parser.name
        self.output_file_path = Parser.output_file_path

        self.formated_data = []
        self.formated_dict = dict()
        self.download()


    def download(self):
        # retrives .gz archive from given URL
        url = URL
        target_path = ARCHIVE_NAME
        response = requests.get(url, stream=True)
        # if file was retrieved successfully, open archive
        if response.status_code == OK:
            with open(target_path, 'wb') as f:
                f.write(response.raw.read())
            with gzip.open(target_path, 'rb') as f_gzip:
                # With the archive opened, split its content on newline character
                self.formated_data = f_gzip.read().decode('utf-8').split('\n')
                # the for every line in the file, split its content on tabulation character and keep only
                # the 3 first entries
                self.formated_data = [value.split('\t')[:3] for value in self.formated_data]
                # remove last value of formated_data because it contains an empty line
                # which is necessary due to posix standards
                self.formated_data.pop()
            # from the 2 ip adresses, return the adress range in slash notation
            [self.get_ranges(line) for line in self.formated_data]
            location = str(self.output_file_path + self.output_file_name).strip() + ".json"
            # creates .json file from name given in CLI at destination also given in CLI
            with open(location, "w") as outfile:
                json.dump(self.formated_dict, outfile)
            os.remove(ARCHIVE_NAME)

    def get_ranges(self, raw):
        ranges = list(self.get_range(raw))
        current_asn = int(raw[2])
        [self.format_values(x, current_asn) for x in ranges]

    def format_values(self, range_ite, asn):
        self.formated_dict.update( { str(range_ite): int(asn) })

    def get_range(self, ip):
        if ipaddress.ip_address(ip[0]).version == 4:
            return ipaddress.summarize_address_range(ipaddress.IPv4Address(ip[0]), ipaddress.IPv4Address(ip[1]))
        else:
            return ipaddress.summarize_address_range(ipaddress.IPv6Address(ip[0]), ipaddress.IPv6Address(ip[1]))


if __name__ == '__main__':
    arg_parser = parser.Parser()
    ip_json_creator = IpJsonCreator(arg_parser)
