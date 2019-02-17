# Linux systemcalls

Please do not use this as a reference. These are just my personal notes.

## File access

### Low-level

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


