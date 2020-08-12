#!/usr/bin/env python3

import argparse

from i3ipc import Connection


def parse_args():
    parser = argparse.ArgumentParser(
        description=
        'cycle focused windows in current workspace on i3 Window Manager')

    parser.add_argument('-p',
                        '--prev',
                        help='focus the previous window',
                        action='store_true')

    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    inc = -1 if args.prev else 1

    i3 = Connection()

    focused = i3.get_tree().find_focused()

    containers = focused.workspace().descendants()

    index = containers.index(focused)

    containers[index + inc].command('focus')


if __name__ == "__main__":
    main()
