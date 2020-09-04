#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

import socket
import time
# import ConfigParser #for Python2
import configparser #for Python3
import json

def main():

    # setting of configparser object
    # config = ConfigParser.ConfigParser() #for Python2
    config = configparser.ConfigParser() #for Python3

    # read Config.ini
    config.read("./Config.ini")

    # reading parameter of Config.ini
    IPaddress = config.get('Settings','IPaddress')
    Port = config.get('Settings','Port')
    Port = int(Port)
    print("IPaddr = [{}] Port = [{}]".format(IPaddress, Port))

    # setting of socket object
    Socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # setting of IPaddress and Port
    Socket_client.connect((IPaddress, Port))

    # inicialize result data
    result_data = ""
    
    # setting of json format data to send RSNPUnit
    send_data = {"data":[{"ac_id":"1","ac":"robot_state","re_id":"1","re":"","co":""}]}

    while True:
        # input data
        print("Input data and enter")
        result_data = input()

        # set result data
        send_data["data"][0]["re"] = result_data
        print(send_data["data"][0]["re"])

        # to bytes
        send_data_byte = bytes(json.dumps(send_data).encode())

        # send data to RSNPUnit by Socket communication
        Socket_client.send(send_data_byte)

        #only print data
        print("send_data: " + str(send_data))
        print()


if __name__ == "__main__":
    main()