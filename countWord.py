# Filipe Nogueira
# input and output file
inputFile = open(r"C:\Users\User\Documents\python\sample.txt", "r")
outputFile = open(r"C:\Users\User\Documents\python\countWord.txt", "w")

# read and count
wordCount = {}
for line in inputFile:
    line = line.replace('"', '').replace('"', '').replace(',', '').replace('.', '').replace('--', '').replace('-', '').replace('!', '').replace('?', '')
    words = line.split()
    for word in words:
        if word not in wordCount:
            wordCount[word] = 1
        else:
            wordCount[word] += 1

# sort frequency
def count(wordFrenquency):
    return wordFrenquency[1]

sorted_words = sorted(wordCount.items(), reverse=True, key=count)

# write 
outputFile.write("Word\tFrequency\n")
for word, count in sorted_words:
    outputFile.write(f"{word}\t{count}\n")

# close
inputFile.close()
outputFile.close()