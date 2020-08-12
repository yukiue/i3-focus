#!/usr/bin/env python3

from i3ipc import Connection, Event

i3 = Connection()

tree = i3.get_tree()

# current
focused = tree.find_focused()

containers = focused.workspace().descendants()

print(containers)
print(focused)

index = containers.index(focused)

containers[index + 1].command('focus')
