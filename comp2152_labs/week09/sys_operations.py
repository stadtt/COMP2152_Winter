#sys_operations
import os
import platform
import socket

print(f"Machine Type: {platform.machine()}\n")
print(f"CPU Architecture: {platform.architecture()}\n")

socket.setdefaulttimeout(50)
print(f"CPU Architecture: {socket.getdefaulttimeout()}\n")

print(f"OS Type: {os.name}\n")
print(f"OS Name: {platform.system()}\n")
print()