# searchfile = open("forbidden.txt", "r")
# for line in searchfile:
#   if "porn" in line:
#       print("explicit found")
# searchfile.close()

# line = "helping webmix contains vigra"
# element  = "vigra"
# if element in line:
#   print("bad")

import json
from profanity_check import predict, predict_prob

with open("demo.json") as json_file:
    data = json.load(json_file)
    webmix = data["webmixes"]
    #print(type(webmix))

    #this is for the comments of each webmix
    # for index, element in enumerate(webmix):
    #     comment = (element.get("comments"))
    #     for attribute in comment:
    #         print((attribute.values()))
            #print(predict(attribute.values()))
        

        # for attribute in element.values():
        #     print(attribute)

        #comment = (element.get("comments"))
        #print(value)
        # print(comment)
        
        #print(type(comment))
        #print(element.get("name"))
        #print(type(element.get("comments")))
        

            
        #print(element.get("comments").get("name"))
        # check = predict(element)
        # print(check)
        #print(element["name"])
        #add each attribute to a list and feed the list to predict
        

        # name  = element["name"]
        # check = predict([name])
        # print(check)

    #this is for the attributes of each webmix    
    searchfile = open("forbidden.txt", "r")
    #this triple loop does not work, should store the values of the list in a different data structure so it is easy to access
    badWords = []
    for line in searchfile:
        forbidden = line.rstrip("\n")
        badWords.append(forbidden)
    #print(badWords)
    

    
    
    for index, element in enumerate(webmix):
        profaneFlag = False
        params = []
        print(element.values)
        # print(type(element.values))
        # if(predict(parameters)== 1):
        #     print('YES')
        if(predict([element['name']]) == 1):
            profaneFlag = True
        if(predict([element['publicName']]) == 1):
            profaneFlag = True
        if(predict([element['description']]) == 1):
            profaneFlag = True
        if(predict([element['tags']]) == 1):
            profaneFlag = True

        if(profaneFlag == True):
            print("Webmix #" + str(index) + " was flagged for profanity in the fields")

        comment = (element.get("comments"))
        for attribute in comment:
            commentFlag = False
            #print((attribute.values()))
            if(any(predict(attribute.values())) == 1):
                commentFlag = True

            if(commentFlag == True):
                print("Webmix #" + str(index) + " was flagged for profanity in the comments")
                break

        for i in range(len(badWords)):
            ourFlag = False
            if(badWords[i] in element['name']):
                ourFlag = True
            if(badWords[i] in element['publicName']):
                ourFlag = True
            if(badWords[i] in element['description']):
                ourFlag = True
            if(badWords[i] in element['tags']):
                ourFlag = True

            if(ourFlag == True):
                print("Webmix #" + str(index) + " was flagged by our list in the fields for the word: " + badWords[i])
                

            comment = (element.get("comments"))
            for attribute in comment:
                #print(badWords[i])
                ourCommentFlag = False
                #I don't understand why I cannot compare bad words to all the attribute.values()
                #print((attribute.values()))
                #print(badWords[i])
                #print(attribute)
                if(badWords[i] in attribute['name']):
                    ourCommentFlag = True
                if(badWords[i] in attribute['text']):
                    ourCommentFlag = True
                    #print(badWords[i])
                
                if(ourCommentFlag == True):
                    print("Webmix #" + str(index) + " was flagged by our list in the comments for the word: " + badWords[i])
                    break

        
        
        
        
        # comment = (element.get("comments"))
        # for attribute in comment:
        #     check = (predict(attribute.values()))
        #     print(attribute)
        #     if(check.any() == 1):
        #         commentFlag = True
        #         print("Bad comment in webmix # " + str(index))
 # print(element.values())
        # predict(element.values())
        # print(predict(element.values()))
    # for element in webmix:
    #   print(element["id"])
        #print(webmix["name"])