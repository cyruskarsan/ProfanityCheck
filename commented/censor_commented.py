from profanity_check import predict, predict_prob
import json
import sys

def check(input):
    explictMix = False
    
    #stores the final dictionary containing which webmixes are explict
    result = {}
    #counting the number of explict webmixes for formating of result
    count =0

    #this is for the attributes of each webmix    
    searchfile = open("forbidden.txt", "r")

    #badWords is a list with all of our bad words from the forbidden text file
    badWords = []
    for line in searchfile:
        forbidden = line.rstrip("\n")
        badWords.append(forbidden)

    #opens and closes the JSON file (when not sending data via POST)
    # with open(input) as json_file:
    #     this is a dictionary
    #     data = json.load(json_file)
    #     this is a list
    #     webmix = data["webmixes"]
   
    webmix = input["webmixes"] 
     
    #creates a numerical list of the items in 'webmix' which I have called element
    for index, element in enumerate(webmix):

        #using profanity-check to see if there are explicts
        profaneFlag = False
        if(predict([element['name']]) == 1):
            profaneFlag = True
            result[count] = {
                    'webmix #' : index,
                    'section' : 'webmix name',
                    'explict' : element['name']
                }
            count= count+1
        if(predict([element['publicName']]) == 1):
            profaneFlag = True
            result[count] = {
                    'webmix #' : index,
                    'section' : 'public name',
                    'explict' : element['publicName']
                }
            count= count+1
        if(predict([element['description']]) == 1):
            profaneFlag = True
            result[count] = {
                    'webmix #' : index,
                    'section' : 'description',
                    'explict' : element['description']
                }
            count= count+1

        if(predict([element['tags']]) == 1):
            profaneFlag = True
            result[count] = {
                    'webmix #' : index,
                    'section' : 'tags',
                    'explict' : element['tags']
                }
            count= count+1

        #(obslete) above prints more specfics 
        # prints which webmix contains explicts
        # if(profaneFlag == True):
        #     result[count] = {
        #             'webmix #' : index,
        #             'section' : 'fields',
        #             'explict' : 'tbd'
        #         }
        #     count= count+1
        #     print("Webmix #" + str(index) + " was flagged for profanity in the fields")

        #checking for profanity in the comments
        comment = (element.get("comments"))
        for attribute in comment:

            #comment flag no longer necessary since we check each attribute
            # commentFlag = False

            #a better way to check for profanity but does not give us the profane word :(
            # if(any(predict(attribute.values())) == 1):
            #     commentFlag = True
            
            #the manual way of checking each attribute
            if(predict([attribute['name']])==1):
                commentFlag = True
                result[count] = {
                    'webmix #' : index,
                    'section' : 'comments',
                    'explict' : attribute['name']
                }
                count = count+1

            #I'm assuming this check is not necessary because time (intuitively) can only contain integers
            # if(predict([attribute['time']])==1):
            #     commentFlag = True
            #     result[count] = {
            #         'webmix #' : index,
            #         'section' : 'comments',
            #         'explict' : attribute['time']
            #     }
            #     count = count+1

            if(predict([attribute['text']])==1):
                commentFlag = True
                result[count] = {
                    'webmix #' : index,
                    'section' : 'comments',
                    'explict' : attribute['text']
                }
                count = count+1

            # used for debugging
            # if(commentFlag == True):
            #     result[count] = {
            #         'webmix #' : index,
            #         'section' : 'comments',
            #         'explict' : 'tbd'
            #     }
            #     count = count+1
            #     print("Webmix #" + str(index) + " was flagged for profanity in the comments")
            #     break

        #using our list of words for as a check for profanity (can probably be put in a different function)
        for i in range(len(badWords)):
            ourFlag = False
            if(badWords[i] in element['name'].lower()):
                ourFlag = True
            if(badWords[i] in element['publicName'].lower()):
                ourFlag = True
            if(badWords[i] in element['description'].lower()):
                ourFlag = True
            if(badWords[i] in element['tags'].lower()):
                ourFlag = True

            if(ourFlag == True):
                result[count] = {
                    'webmix #' : index,
                    'section' :'fields',
                    'explict' : badWords[i]
                }
                count = count+1

                #print statement for debugging
                #print("Webmix #" + str(index) + " was flagged by our list in the fields for the word: " + badWords[i])
                
            #checking for explicts in our list of words
            comment = (element.get("comments"))
            for attribute in comment:
                #print(badWords[i])
                ourCommentFlag = False

                #I don't understand why I cannot compare bad words to all the attribute.values()
                #print((attribute.values()))
                #print(badWords[i])
                #print(attribute)

                if(badWords[i] in attribute['name'].lower()):
                    ourCommentFlag = True
                if(badWords[i] in attribute['text'].lower()):
                    ourCommentFlag = True
                    #print(badWords[i])
                
                if(ourCommentFlag == True):
                    result[count] = {
                    'webmix #' : index,
                    'section' : 'comments',
                    'explict' : badWords[i]
                }
                    count = count+1

                    #print statement for debugging
                    #print("Webmix #" + str(index) + " was flagged by our list in the comments for the word: " + badWords[i])
                    break
    return (result)

def main():
    #this is a generic example, when the data is sent via POST, it will override this file but look for the same file type
    with open("demo.json", "r") as read_file:
        data = json.load(read_file)
        print("\n")
        check(data)
main()