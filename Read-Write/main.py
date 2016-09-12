fw = open('file.txt', 'w')

fw.write('First line\n')
fw.write('Second line\n')
fw.close()

fr = open('file.txt', 'r')

text = fr.read()
print(text)
fr.close()
