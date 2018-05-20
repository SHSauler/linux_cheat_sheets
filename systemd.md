# Systemd overview

## Targets

### Mapping of targets with SysV runlevels

```bash
bash$ ls -l runlevel* | cut -d" " -f 10-
runlevel0.target -> poweroff.target
runlevel1.target -> rescue.target
runlevel2.target -> multi-user.target
runlevel3.target -> multi-user.target
runlevel4.target -> multi-user.target
runlevel5.target -> graphical.target
runlevel6.target -> reboot.target
```

### List targets

Show current target list.

```bash
bash$ systemctl list-units --type=target
UNIT                LOAD   ACTIVE SUB    DESCRIPTION                           
basic.target        loaded active active Basic System                          
bluetooth.target    loaded active active Bluetooth                             
cryptsetup.target   loaded active active Local Encrypted Volumes               
[...]         

LOAD   = Reflects whether the unit definition was properly loaded.
ACTIVE = The high-level unit activation state, i.e. generalization of SUB.
SUB    = The low-level unit activation state, values depend on unit type.
```

Targets live in `/usr/lib/systemd/system`

```bash
bash$ ls -l *.target | head -5
-rw-r--r-- 1 root root 919 Apr  9 14:08 basic.target
-rw-r--r-- 1 root root 419 Apr  9 14:08 bluetooth.target
-rw-r--r-- 1 root root 465 Apr  9 14:08 cryptsetup-pre.target
-rw-r--r-- 1 root root 412 Apr  9 14:08 cryptsetup.target
```

### Show and change default

```bash
bash$ systemctl get-default
graphical.target
```

To change the current target for _this session only_
```bash
bash$ systemctl isolate graphical.target
```

To set a new default

```bash
bash# systemctl set-default multi-user.target
```
