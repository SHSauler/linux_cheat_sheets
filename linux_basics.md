Command Line Basics
-------------------

The **shell** is a command line interpreter. In Linux we commonly use **bash** (Bourne Again Shell), but there are some other ones. Here is a short history of past and current shells:

| Shell Name | Description                                                                                                            |
|------------|------------------------------------------------------------------------------------------------------------------------|
| sh         | Bourne shell (Stephen R. Bourne, 1977) was published with Unix V7                                                      |
| csh        | C Shell (Bill Joy, 1978); features like stopping and restarting commands in foreground or background; aliases, history |
| tcsh       | TENEX C Shell (1981), had some features like filename autocompletion                                                   |
| ksh        | Korn shell (David Korn, 1983); merge of C and Bourne shell, orginally only commercially available                      |
| bash       | Bourne Again Shell (1989), part of the GNU project, most common in Linux today, Windows port is part of Cygwin         |
| zsh        | Z shell (Paul Falstad, 1990); merge of the improvements from bash, csh, tcsh and ksh                                   |

(Source: https://de.wikipedia.org/wiki/Unix-Shell\)

When we talk about shells, we have to differentiate between:

| Types of default shells   | Description                            |
|---------------------------|----------------------------------------|
| Default interactive shell | Shell for users                        |
| Default system shell      | Shell in which system executes scripts |

-	We can determine the shell via the shell variable $SHELL
-	Variable in zsh

### Type of Commands

There are two kinds of commands:

| Type of command | Description                                         |
|-----------------|-----------------------------------------------------|
| Built-in        | Shell-internal commands, differ from shell to shell |
| External        | Commands that are not part of the shell itself      |

#### Examples of built-in commands

| Command | Description             |
|---------|-------------------------|
| cd      | Change directory        |
| pwd     | Print working directory |

#### Examples of external commands

| Command | Description              |
|---------|--------------------------|
| uname   | Print system information |
| passwd  | Change user password     |

#### Excursion: Variables

Bash, like programming languages, makes use of variables. It has no data types, that means you can put text or integers (numbers).

Syntax: `KEY=value1:value2:valueN` or `KEY=value`

Example: `$ VARIABLE=123` and `$ echo $VARIABLE`

There are two ways to get a variable with the result of a command or a series of commands (e.g. connected with pipes:)

`contentofpasswd=$(cat /etc/passwd)` and

contentofpasswd=\`cat /etc/passwd\` (I can't use backticks here or it gets broken at the command, please help!)

Navigation
----------

### Terminal keys

| Key(s)       | Description                          |
|--------------|--------------------------------------|
| `TAB`        | command auto completion              |
| `Ctrl` + `l` | clear screen                         |
| `q`          | close text window (i.e. more & less) |
| `Ctrl` + `c` | cancel command execution             |
| `Ctrl` + `z` | interrupt command execution          |
| `Ctrl` + `u` | clear prompt line                    |


### Movement

| Key-Combo     | Action                             |
|---------------|------------------------------------|
| `Ctrl+a`      | Move to **start** of line          |
| `Ctrl+e`      | Move to **end** of line            |
| `Left Arrow`  | Move **left**, back one char       |
| `Ctrl+b`      | Move **left**; **[b]ack** one char |
| `Right Arrow` | Move right one char                |
| `Ctrl+f`      | Move right one char; **[f]orward** |

### Modification

| Key-Combo      | Action                                                 |
|----------------|--------------------------------------------------------|
| `Ctrl+t`       | **Transpose**; switch char before with current char    |
| `ESC` then `u` | Make **upercase** from current position to end of line |

### Deletion

| Key-Combo              | Action                                    |
|------------------------|-------------------------------------------|
| `Ctrl+d`               | Delete under cursor                       |
| `Ctrl+k`               | Delete from cursor to end of line         |
| `Ctrl-x` + `Backspace` | Delete from beginning to current position |

### Editing in the editor

| Key-Combo              | Action              |
|------------------------|---------------------|
| `Ctrl+x` then `Ctrl+e` | Open line in editor |

Book says default editor may be defined in `$FCEDIT` or `$EDITOR` variables. On Debian Stable they are not and `nano` is used.

#### Excursion: Editors

There are many text editors in Linux. Popular ones are* *vim*: ships pretty everywhere* *emacs*: Default GNU text editor and* *nano*: simple text editor in Debian

**Hint**: To exit *vim* without saving changes, type `:q!`

### Getting previously executed Commands

Sometimes, instead of typing it again, you want to execute a command you already typed earlier. It's stored in `~/.bash_history` only after exit.

| Key-Combo | Action                                      |
|-----------|---------------------------------------------|
| history   | show history of commands                    |
| !!        | repeat last command                         |
| !1234     | Execute command 1234 from history           |
| !-2       | Execute the second to last command          |
| `Ctrl+R`  | Search for command in your history backward |
| `Ctrl+S`  | Search for command in history forward\*     |

\* The forward search can freeze your terminal. Press `Ctrl+Q` to resume.

Commands
--------

###Getting help and finding programs

| Command        | Description                                   |
|----------------|-----------------------------------------------|
| man            | reference manual                              |
| man -f         | look up single command                        |
| apropos        | find command name                             |
| whatis         | alias of man -f                               |
| info coreutils | GNU utilities manual                          |
| whereis        | locate source, binary and man page of program |
| which          | return binary location of program             |

### Streams, Pipes and Redirection

| Type        | Description                                      |
|-------------|--------------------------------------------------|
| streams     | IO stream of characters: *stdin, stdout, stderr* |
| pipes       | way to further process IO streams                |
| redirection | way to redirect the IO streams                   |

#### IO streams

IO streams are a stream of characters. Their *descriptor* is the number that can be used in redirection.

| Type   | Description                                       | Descriptor |
|--------|---------------------------------------------------|------------|
| stdin  | standard input stream (e.g. keyboard)             | 0          |
| stdout | standard output stream (e.g. displayed on screen) | 1          |
| stderr | standard error stream                             | 2          |

(Sometimes the names of the IO streams are given in uppercase, e.g. STDIN, but refer to the same thing.)

#### Redirection

| Operator | Description                                      | Example                                            |
|----------|--------------------------------------------------|----------------------------------------------------|
| \>       | Create new file with *stdout*                    | cat /etc/passwd > passwdfile                       |
| >>       | Append *sdout* to file if exists; else create it | cat /etc/passwd >> passwdfile                      |
| 1>       | Redirect *stdout*                                | echo "taH pagh taHbe'!" 1> hamlet.txt              |
| 2>       | Redirect *stderr*                                | As non-root: touch /etc/nonono 2> error; cat error |
| &>       | Redirect both *stdout* and *stderr*              | ./somescript.sh &> logfile.log                     |
| \<       | Send content of file as *stdin* for command      | sort < unsorted_file.txt                           |
| \<\<     | Accept multiline text                            | echo \<< EOF multiple lines here EOF               |
| <>       | Use file as *stdin* and *stdout*                 | Never used that in practise                        |

**Examples**

`./program.py 1> /dev/null 2>output` Redirects *stdout* to never show up, error to file *output*

##### xargs

`xargs - build and execute command lines from standard input`

```bash
# find files that belong to a user and delete their files (careful!)
find / -user exampleuser | xargs -d "\n" rm

# find all files ending in test and see whether they contain "hello"
find . -name "*test" | xargs grep "hello"
```

#### Pipes

Pipes take the output of the first command and give it to the second.

`echo $PATH | tee path.txt`

Processing text with filters
============================

### Combining files

| Type  | Description                                        |
|-------|----------------------------------------------------|
| cat   | concatenate files and print on the standard output |
| tac   | Reverse cat                                        |
| join  | join lines of two files on a common field          |
| paste | merge lines of files- line by line                 |

#### cat

| Option | Description             |
|--------|-------------------------|
| -E     | Show line endings       |
| -n     | Number lines            |
| -s     | Minimize blank lines    |
| -T     | Show special characters |

`cat -sn testpage.txt`

#### join

`sort [OPTION]... [FILE]...`

| Option  | Description      |
|---------|------------------|
| -i      | Ignore case      |
| -t CHAR | Choose seperator |

```bash

 $ ~/training/joinexample$ join <(sort stockname) <(sort stockquote)
NFLX Netflix Inc 102.71 +4.16 / +4.22
SAP SAP SE 90.86 -0.55 / -0.60%
TSLA Tesla Motors Inc 213.54 +9.51 / +4.66%
TWTR Twitter Inc 24.01 +0.96 / +4.16\
```

### Transforming files

| Command  | Description                               |
|----------|-------------------------------------------|
| sort     | sort file                                 |
| split    | split file into pieces                    |
| tr       | change individual characters from *stdin* |
| uniq     | Delete duplicates                         |
| od       | octal dump, output file in base 8         |
| expand   | Convert tabs to spaces (e.g. padding)     |
| unexpand | Convert spaces to tabs                    |

##### Sort command

`sort [OPTION]... [FILE]...`

| Option | Description           |
|--------|-----------------------|
| -b     | Ignore leading blanks |
| -f     | Ignore case           |
| -M     | Month sort            |
| -n     | Numberic sort         |
| -r     | Reverse sort          |

##### Sort command

`split [OPTION]... [INPUT [PREFIX]]`

| Option   | Description                            |
|----------|----------------------------------------|
| -b BYTES | split by bytes                         |
| -l N     | split after N lines                    |
| -C BYTES | Line-sized chunks (not breaking lines) |

`ultem@actual:~/training/splitexample$ cat testpage.txt | split -l 4`

##### tr command

```
$:~/training$ cat -s testpage.txt | sed "/^$/d" | tr K R | head
Ring. Sure we thanke you.

$:~/training$ cat -s testpage.txt | sed "/^$/d" | tr -d you | head

```

##### expand

```
$:~/training/expand$ cat -T exthis
^I^I^I^Ithis has 4 tabs
$:~/training/expand$ cat -T <(expand exthis)
    this has 4 tabs
```

### Formatting text

| Command | Description                                 |
|---------|---------------------------------------------|
| nl      | number lines of files                       |
| pr      | convert text files for printing             |
| fmt     | optimal text formatting, select line length |

### Viewing files

| Command | Description                     |
|---------|---------------------------------|
| head    | number lines of files           |
| tail    | convert text files for printing |
| less    | convert text files for printing |

### Summarizing files

| Command | Description                     |
|---------|---------------------------------|
| cut     | number lines of files           |
| wc      | convert text files for printing |

Using Regular Expressions
=========================

With regular expressions you can *match patterns in a text*. This allows you to, for example, replace all occurrences of your username in a logfile with that of another user.

| Command | Description                                       |
|---------|---------------------------------------------------|
| grep    | print lines matching a pattern                    |
| sed     | stream editor for filtering and transforming text |

grep
----

`grep [OPTIONS] PATTERN [FILE...]`

| Option | Description                                            |
|--------|--------------------------------------------------------|
| -c     | Only display number of lines matching                  |
| -f     | Takes file instead of *stdin*                          |
| -i     | Ignore case                                            |
| -F     | Instead of regex, use fixed string -> `fgrep`          |
| -E     | Extended regex, -> `egrep`                             |
| -r     | Search recursively in folder and subfolders -> `rgrep` |

Examples:

```bash
#find your username in /etc/passwd
grep "yourusername" /etc/passwd

#get all usernames starting with s
grep "^s\w*:" /etc/passwd

#case insensitive search for "you"
grep -i "you" henry5.txt

#search all Kings in the training directory recursively
grep -ri "king" *
```

sed
---

`sed [OPTION]... {script-only-if-no-other-script} [input-file]...`

| Option | Description                                            |
|--------|--------------------------------------------------------|
| -c     | Only display number of lines matching                  |
| -f     | Takes file instead of *stdin*                          |
| -i     | Ignore case                                            |
| -F     | Instead of regex, use fixed string -> `fgrep`          |
| -E     | Extended regex, -> `egrep`                             |
| -r     | Search recursively in folder and subfolders -> `rgrep` |

`sed '/^$/d' input.txt | nl`
