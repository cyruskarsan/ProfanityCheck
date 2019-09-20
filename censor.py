from profanity_check import predict, predict_prob
import json
import sys

def check(input, badWords):
    explictMix = False
    
    #stores the final dictionary containing which webmixes are explict
    result = {}
    #counting the number of explict webmixes for formating of result
    count =0
    webmix = input["webmixes"] 
    
    #creates a numerical list of the items in 'webmix' which I have called element
    for index, element in enumerate(webmix):
        #using profanity-check to see if there are explicts
        profaneFlag = False
        if(predict([element['name']]) == 1):
            profaneFlag = True
            result[count] = {
                    'webmix id' : element['id'],
                    'section' : 'webmix name',
                    'explict' : element['name']
                }
            count= count+1

        if(predict([element['publicName']]) == 1):
            profaneFlag = True
            result[count] = {
                    'webmix id' : element['id'],
                    'section' : 'public name',
                    'explict' : element['publicName']
                }
            count= count+1

        if(predict([element['description']]) == 1):
            profaneFlag = True
            result[count] = {
                    'webmix id' : element['id'],
                    'section' : 'description',
                    'explict' : element['description']
                }
            count= count+1

        if(predict([element['tags']]) == 1):
            profaneFlag = True
            result[count] = {
                    'webmix id' : element['id'],
                    'section' : 'tags',
                    'explict' : element['tags']
                }
            count= count+1

        #checking for profanity in the comments
        comment = (element.get("comments"))
        for attribute in comment:
            #the manual way of checking each attribute
            if(predict([attribute['name']])==1):
                commentFlag = True
                result[count] = {
                    'webmix id' : element['id'],
                    'section' : 'comments',
                    'explict' : attribute['name']
                }
                count = count+1

            if(predict([attribute['text']])==1):
                commentFlag = True
                result[count] = {
                    'webmix id' : element['id'],
                    'section' : 'comments',
                    'explict' : attribute['text']
                }
                count = count+1

        #using our list of words for as a check for profanity (can probably be put in a different function)
        # if("fart" in badWords):
        #     print("found")
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
                    'webmix id' : element['id'],
                    'section' :'fields',
                    'explict' : badWords[i]
                }
                count = count+1

            #checking for explicts in our list of words
            comment = (element.get("comments"))
            for attribute in comment:
                ourCommentFlag = False

                if(badWords[i] in attribute['name'].lower()):
                    ourCommentFlag = True
                if(badWords[i] in attribute['text'].lower()):
                    ourCommentFlag = True
                
                if(ourCommentFlag == True):
                    result[count] = {
                    'webmix id' : element['id'],
                    'section' : 'comments',
                    'explict' : badWords[i]
                }
                    count = count+1
                    break
    
    return (result)

def main():
    #this is a generic example, when the data is sent via POST, it will override this file but look for the same file type
    with open("demo.json", "r") as read_file:
        data = json.load(read_file)
        print("\n")
        tempList = []
        check(data, tempList)

main()