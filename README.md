# health-checks
Scripts that check the health of my computers

This repo will be populated with lots of fancy checks!


health_checks.py contain functions that check the system for errors.

health_checks functions include:

check_reboot():	Returns True if a reboot is required

check_disk_full(disk, min_gb, min_percent): Returns True if there isn't enough disk space, False otherwise

check_root_full(): Returns  True if root partition is full, False otherwise

check_cpu_constrained(): Returns True if the CPU is having too much usage, False otherwise

check_no_network(): Return True if it fail's to resolve Google's URL, False otherwise

check_system_logs(): Return True if critical errors are found in kern or sys logs, False otherwise

After running checks "Everything is Ok" will be printed if no errors,
otherwise corresponding error message will be displayed.

Return code: 1 if errors are found and 0 if none.
