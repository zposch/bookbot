bookPath = "books/frankenstein.txt" # File path for .txt file to read

def main():

    words = text(bookPath)
    numWords = wordCount(words)
    characterFormat(words)
    characterList = characterFormat(words)
    numCharacters = characterCount(characterList)
    printReport(numWords, numCharacters)

    return True

def printReport(wordCount, characterCount): # Prints out a full report for the number of each character and word count
    print(f"--- Begin report of {bookPath} ---")
    print(f"{wordCount} words found in the document")
    for character in characterCount:
        print(f"The '{character['character']}' character was found {character['count']} times")

    return True

def text(path): # Opens the document and reads the file into file_contents
    with open(path) as f:
        fileContents = f.read()

    return fileContents.lower()

def wordCount(text): # Takes the fileContents as input and returns the number of words in the file by using the split() method
    textList = text.split()
    return len(textList)

def sortOn(dict):
    return dict["count"]


def characterCount(characterList): # Takes a list of characters from characterFormat() and returns a dictionary ofeach alphabetical character and the number of occurences 
    filteredList = []

    for character in characterList:
        if character.isalpha():
            filteredList.append(character)

    characterSet = set(filteredList)
    characterDict = dict.fromkeys(characterSet, 0)

    for character in characterList:
        if character in characterDict:
            characterDict[character] += 1
        else:
            continue

    dictList = []
    for key in characterDict: # Converting the character
        listDict = {"character": key, "count": characterDict[key]}
        dictList.append(listDict)
    
    dictList.sort(reverse=True, key=sortOn)
    
    return dictList

def characterFormat(text): # Takes the wordCount as input and further splits it into characters
    wordList = text.split()
    characters = []

    for word in wordList:
        words = list(word)
        for character in words:
            character.lower()
            characters.append(character)
    
    return characters

main()