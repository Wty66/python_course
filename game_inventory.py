from __future__ import print_function


def display_inventory(inv):
    total = 0
    for key, val in inv.iteritems():
        print(key, val)
        total += val
    print('Total number of items:', total)


def add_to_inventory(inv, dragon_loot):
    for i in dragon_loot:
        if i in inv:
            inv[i] += 1
        else:
            inv[i] = 1
    return inv


def main():
    inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dragger': 1, 'arrow': 12}
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    display_inventory(inv)
    add_to_inventory(inv, dragon_loot)
    display_inventory(inv)
    pass

if __name__ == '__main__':
    main()

