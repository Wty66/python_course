with tarfile.open('tarfile_add.tar',mode='w|gz') as t:
    [t.add(item) for item in glob.glob('*.txt')]
    print(t.getnames())

