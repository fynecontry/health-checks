#!/usr/bin/env python3
import os
import shutil
import sys
import psutil
import socket


def check_reboot():
    """Returns True if a reboot is required"""
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
    """Returns True if there isn't enough disk space, False otherwise."""
    du = shutil.disk_usage(disk)
    #Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    #Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if gigabytes_free < min_gb or percent_free < min_percent:
        return True
    return False

def check_root_full():
    """Returns  True if root partition is full, False otherwise"""
    return check_disk_full(disk="/", min_gb=2, min_percent=10)

def check_cpu_constrained():
    """Returns True if the CPU is having too much usage, False otherwise"""
    return psutil.cpu_percent(1) > 75

def check_no_network():
    """Return True if it fail's to resolve Google's URL, False otherwise"""
    try:
        socket.gethostbyname("www.google.com")
        return False
    except:
        return True

def check_system_logs():
    """Return True if critical errors are found in kern or sys logs, False otherwise"""
    critical_error_present = False
    for log_path in ['/var/log/kern.log', '/var/log/syslog']:
        try:
            with open(log_path) as log_file:
                for line in log_file:
                    if 'critical' in line.lower():
                        print(f'{line}')
                        critical_error_present = True
        except:
            print(f'Could not locate log file: {log_path}')
    return critical_error_present

def main():
    checks=[
        (check_reboot,"Pending Reboot"),
        (check_root_full, "Root partition full"),
        (check_cpu_constrained, "CPU load is too high"),
        (check_no_network, "No working network"),
        (check_system_logs, "Errors found in logs"),
    ]

    everything_ok = True
    for check, msg in checks:
        if check():
            print(msg)
            everything_ok = False

    if not everything_ok:
        sys.exit(1)

    print('Everything is OK.')
    sys.exit(0)

main()
