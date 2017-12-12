#
# filename: concordance.py
#
# Ferdinand Enario ftenario@yahoo.com
#
# Description: Concordance Program
#
# 1. Open and read a file specified from the command line
# 2. Analyze the file and print a sorted list of unique words
#		followed by a sorted list of the unique line numbers where 
#		each word occdurs in the file. For this purpose,
#		words are defined as continuous sequence of letters.
# 3. Must be able to handle files up to 10Mb
# 4. Should be case sensitive
# 5. Should be able to handle file gracefully
import sys
import mimetypes
import re

def StripChars(word):
    s = re.sub("[!,.'?\"$'%&#*-0123456789]","",word)
    return s

if len(sys.argv) != 2:
    print("Not enough argument passed... exiting")
    exit(0)

else:
    #Get the first passed argument
    file = sys.argv[1]
    mime = mimetypes.guess_type(file)
    cnt = 0

    if (mime[0] == 'text/plain'):
        #open the file, read and close the file
        d = dict()
        with open(file) as infile:

        #f = open(file, "r")
        #string_read = f.read()
        #f.close()

            for string_read in infile:
                cnt += 1

                #split the file using the new line
                tmp = string_read.split("\n")
                #decalre a dictionary for later use

                #loop thru thre array
                for line in tmp:
                    #check if line exceeds 200 chars
                    if len(line) > 200:
                        print("Line exceed 200 characters...exiting.")
                        break

                    #split the line
                    words = line.split(' ')

                    #loop thru the words
                    for word in words:
                        word = StripChars(word)
                        word = word.strip().lower()

                        #add the word if not in the dictionary
                        if not d.has_key(word) and word is not '':
                            d[word] = str(cnt)
                        #if the word is in the dictionary, update the line number
                        else:
                            if word is not '' and str(cnt) not in d.get(word):
                                d[word] = d.get(word) + ',' +  str(cnt)

        #print the result
        for k in sorted(d.iterkeys(), key=lambda s: s.lower()):
            print(k + ' ' + d[k])
    else:
        print("Error: Use a text file")
