# Managing users and groups

## Passwd

### /etc/passwd file

```
ultem:x:1000:985:Ultem lives here:/home/ultem:/bin/bash
 (1) (2) (3) (4)         (5)          (6)        (7)

(1) username
(2) password field (empty, see shadow)
(3) UID, User identifier
(4) GID, group identifier
(5) GECOS, comment field with full name
(6) Home directory
(7) Shell

```

### passwd tool

`passwd` tool can give information regarding the account status.

```
$ sudo passwd -S
root P 02/10/2018 -1 -1 -1 -1
bin L 02/10/2018 -1 -1 -1 -1
daemon L 02/10/2018 -1 -1 -1 -1
mail L 02/10/2018 -1 -1 -1 -1
ftp L 02/10/2018 -1 -1 -1 -1

Fields seperated by whitespace:
(1) login name
(2) L = Locked password, NP = No password, P = usable password
(3) date of last password change
(4) Minimum age in d
(5) Maximum age in d
(6) Warning period in d
(7) Inactivity period in d
```
## Shadow

## Group

## Skeleton
