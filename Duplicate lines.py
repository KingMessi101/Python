outputFile  = open('UpdatedFile.txt', 'w')

inputFile  = open('Reapeted.txt', 'r')

lines_seen_so_far = set()
print("eliminating duplicate lines.... ")
for line in inputFile:
    if line not in lines_seen_so_far:
        outputFile.write(line)
        lines_seen_so_far.add(line)

inputFile.close()
outputFile.close()