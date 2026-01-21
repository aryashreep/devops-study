# Linux Essentials Cheat Sheet

## 1. File Permissions

### Permission Basics
- **r** = read (4)
- **w** = write (2)
- **x** = execute (1)

Permission format:
-rwxr-xr--
| | | |
| | | └── Others
| | └──── Group
| └────── Owner
└──────── File type


### Common Commands
```bash
ls -l                 # List files with permissions
chmod 644 file.txt    # rw-r--r--
chmod 755 script.sh   # rwxr-xr-x
chmod u+x script.sh   # Add execute to owner
chmod g-w file.txt    # Remove write from group
```

### Ownership
```bash
chown user file.txt
chown user:group file.txt
chown -R user:group /directory
```

### umask
```bash
umask                 # Show default permission mask
umask 022             # Default: files 644, dirs 755
```

## 2. systemctl (systemd) Basics
### Service Management
```bash
systemctl status nginx
systemctl start nginx
systemctl stop nginx
systemctl restart nginx
```

### Enable / Disable at Boot
```bash
systemctl enable nginx
systemctl disable nginx
systemctl is-enabled nginx
```

### View Services
```bash
systemctl list-units --type=service
systemctl list-unit-files
```

### Logs
```bash
journalctl -u nginx
journalctl -u nginx --since today
journalctl -xe
```

## 3. Package Management
### Debian / Ubuntu (apt)
```bash
sudo apt update
sudo apt upgrade
sudo apt install nginx
sudo apt remove nginx
sudo apt purge nginx
sudo apt autoremove
apt search nginx
apt list --installed
```

### RHEL / CentOS / Amazon Linux (yum / dnf)
```bash
sudo yum update
sudo yum install nginx
sudo yum remove nginx
yum search nginx
yum list installed
```

## 4. Useful File & System Commands
```bash
pwd                 # Current directory
cd /path/to/dir     # Change directory
ls -la              # List all files
cp src dest         # Copy files
mv old new          # Move/rename
rm -rf dir          # Delete directory
df -h               # Disk usage
du -sh *            # Directory sizes
free -h             # Memory usage
uptime              # System load
```

## 5. Quick Troubleshooting Tips
 - Permission denied → check ls -l, chmod, chown
 - Service not starting → systemctl status <service>
 - Check logs → journalctl -xe
 - Package issues → run apt update or yum clean all

## 6. Best Practices
 - Use least privilege permissions
 - Avoid chmod 777
 - Stop and disable unused services
 - Remove unused packages to reduce attack surface

## 7. References
 - man chmod
 - man systemctl
 - man apt
 - man yum
