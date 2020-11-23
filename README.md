# i3-focus

A tool to cycle focused windows on [i3 Window Manager](https://i3wm.org/)

## Usage
```
usage: focus.py [-h] [-r] [-c]

cycle focused windows on i3 Window Manager

optional arguments:
  -h, --help     show this help message and exit
  -r, --reverse
  -c, --current
```

- cycle focus between all windows

```shell
$ python3 focus.py
```

- cycle focus between all windows in reverse order

```shell
$ python3 focus.py -r
```
- cycle focus between windows in current workspace

```shell
$ python3 focus.py -c
```

## Example

1. save `focus.py` to ~/.config/i3/
2. add the following lines to `~/.config/i3/config`
```
bindsym Mod1+Control+i exec python3 ~/.config/i3/focus.py -c
bindsym Mod1+Control+r exec python3 ~/.config/i3/focus.py -r
```
