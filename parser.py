# encoding utf-8
import argparse
import sys
import re


class Parser:
    def __init__(self):
        self.parser = ArgParser()
        self.args = self.parser.args
        self.name = self.args.name
        self.output_file_path = self.args.of

    def parse_ip(self, file):
        lines_in_file = []
        with open(file, 'r') as reader:
            lines_in_file = reader.readlines()
        if lines_in_file:
            pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
            ip_in_file = []
            for line in lines_in_file:
                ip = re.findall(pattern, line)
                if ip:
                    ip_in_file.append(ip)

            return ip_in_file

        else:
            print("File not found maybe due to invalid path")
            sys.exit()


class ArgParser:

    __instance = None

    @staticmethod
    def getInstance():
        if ArgParser.__instance is None:
            ArgParser()
        return ArgParser.__instance

    def __init__(self):
        if ArgParser.__instance is None:
            ArgParser.__instance = self

        self._parser = argparse.ArgumentParser()
        self._initArguments()
        if len(sys.argv) == 1:  # [T.L. 2022.01.28] No argument show help and exit
            self._parser.print_help()
            sys.exit()
        else:
            self.args = self._parser.parse_args()

    def _initArguments(self):
        self._parser.add_argument('--name', required=True, type=str,
                                  help='Specifies name of output file  \n\n ex: ./main --name formated_file_name')

        self._parser.add_argument('--of', required=True, type=str,
                                  help='Specifies path of output file  \n\n ex: ./main --of ~/user/destination_of_file')

    def get_outfile_path(self):
        return self.args.of

    def get_name(self):
        return self.args.name
