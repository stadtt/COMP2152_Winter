#sys_operations
import os
import platform
import socket
import sys

print(f"Machine Type: {platform.machine()}\n")
print(f"CPU Architecture: {platform.architecture()}\n")

socket.setdefaulttimeout(50)
print(f"CPU Architecture: {socket.getdefaulttimeout()}\n")

print(f"OS Type: {os.name}\n")
print(f"OS Name: {platform.system()}\n")

print(f"Current PID: {os.getpid()}\n")
print()

file_name = "fdpractice.txt"
file_handler = os.open(file_name, os.O_RDWR | os.O_CREAT)

print(f"[PID: {os.getpid()}] Opened the file_handle: {file_handler}\n")

file_object_TextIO = os.fdopen(file_handler, "w+")
file_object_TextIO.write("some string to write to file\n")
file_object_TextIO.flush()

print(f"\n\n[PID: {os.getpid()}] Forking now...")
pid = 0

if pid == 0:
    print(f"[ Child PID: {os.getpid()}], Parent PID: {os.getppid()}\n")
    os.lseek(file_handler,0 ,0)
    print(f"[Child PID: {os.getpid()}], File Content: {os.read(file_handler,100).decode()}\n")
    os.close(file_handler)
    sys.exit(0)
else:
    print(f"[Parent PID: {os.getppid()}], [Child PID: {os.getpid()}]")
    print("wait for child")
    os.wait()
    print("Child finished")

    file_object_TextIO.close()

sys.exit(0)

