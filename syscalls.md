# Linux systemcalls

Please do not use this as a reference. These are just my personal notes.

## File access

### Low-level

#### Standard streams

```
fd = 0     - stdin
fd = 1     - stdout
fd = 2     - stderr
```

#### Bitwise OR of constants

Flags are bitwise OR'd to combine, e.g.

```
#ifndef O_TRUNC
#define O_TRUNC		00001000	/* not fcntl */
#endif
#ifndef O_APPEND
#define O_APPEND	00002000
#endif

fd = open("filename.txt", O_RDWR| O_TRUNC | O_APPEND)
```

#### Unbuffered IO

* open()
* close()
* read()
* write()

##### [open](http://man7.org/linux/man-pages/man2/open.2.html)

```
int open(const char *pathname, int flags, mode_t mode);

flags:
O_RDONLY   - read only
O_WRONLY   - write only
O_RDWR     - read and write

optional:
O_APPEND   - append to file
O_CREAT    - create file
O_TRUNC    - truncate to zero length if exists
```

##### [close](http://man7.org/linux/man-pages/man2/close.2.html)

Returns the numbers of bytes actually read.

```
int close(int fd);

close(fd)
```

##### [read](http://man7.org/linux/man-pages/man2/read.2.html)

Returns the numbers of bytes actually read.

```
ssize_t read(int fd, void *buf, size_t count);

read(fd, buffer, count)
```

##### [write](http://man7.org/linux/man-pages/man2/write.2.html)

```
ssize_t write(int fd, const void *buf, size_t count);

write(fd, buffer, count)
```
