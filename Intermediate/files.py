f = open('myData.txt','r') #to read
print(f.read()) #this displays the whole file
print(f.readline(),end="") # will display the first line of the file
print(f.readline())

f = open("abc","w") #this adds new data and erase the existing ones
f = open("abc","a") #to append kabisa on the existing data
f.write(" Kabisa")


f = open('myData.txt', 'r')


#2 this code will add data from myfile.txt to abc.txt
f = open('myfile.txt','r')
f1 = open("abc.txt","w")

for data in f:
	f1.write(data)

#on photos
f = open('1.png','rb')
f1 = open('2.png','wb')

for i in f:
	f1.write(i)
 
#4
#Write a program that reads a file, breaks each line into words, strips whitespace and
#punctuation from the words, and converts them to lowercase.

import string

# Function to process the file
def process_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Strip whitespace and break the line into words
                words = line.strip().split()
                # Process each word
                cleaned_words = []
                for word in words:
                    # Remove punctuation using str.translate and string.punctuation
                    word = word.translate(str.maketrans('', '', string.punctuation))
                    # Convert to lowercase
                    word = word.lower()
                    cleaned_words.append(word)
                
                # Output the cleaned words
                print(cleaned_words)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Example usage:
filename = 'myData.txt'  # Replace with your actual file name
process_file(filename)
