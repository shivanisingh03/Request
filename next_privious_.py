import requests
import json

response=requests.get("https://api.merakilearn.org/courses")
saral=response.json()

with open("alldata.json","w") as file:
    json.dump(saral,file,indent=4)

s_no1=1
for i in saral:
    print(s_no1,i["name"],i["id"])
    s_no1+=1
    
identity1=int(input("enter the id number here: "))
print(saral[identity1-1]["name"])
identity=(saral[identity1-1]["id"])

navigation1=input("what do you want privious(p).... or next(n).......")
if navigation1=="p":
    s_no1=1
    for i in saral:
        print(s_no1,i["name"],i["id"])
        s_no1+=1
        
    identity1=int(input("enter the id number here: "))
    print(saral[identity1-1]["name"])
    identity=(saral[identity1-1]["id"])
    
    nevigation2=input("what do you want privious(p)......or next(n)....")
    if nevigation2=="p":

        s_no1=1
        for i in saral:
            print(s_no1,i["name"],i["id"])
            s_no1+=1
            
        identity1=int(input("enter the id number here: "))
        print(saral[identity1-1]["name"])
        identity=(saral[identity1-1]["id"])
        
        
        response1=requests.get("https://api.merakilearn.org/courses/"+str(identity)+"/exercises")
        saral1=response1.json()
        with open("course.json","w") as file1:
            json.dump(saral1,file1,indent=4)
            s_no2=1
            list1=[]
            list2=[]
        for j in saral1["course"]["exercises"]:
            if j["parent_exercise_id"]==None:
                print(s_no2,j["name"])
                print(" ","1. ",j["slug"])
                s_no2+=1
                new_no=1
                list1.append(j)
                list2.append(j)
                continue
            if j["parent_exercise_id"]==j["id"]:
                print(s_no2,j["name"])
                s_no2+=1
                new_no=1
                list1.append(j)
            for k in saral1["course"]["exercises"]:
                if j["parent_exercise_id"]!=["id"]:
                    print(" ",new_no,j["name"])
                    new_no+=1
                    list2.append(j)
                    break
        with open("parent.json","w") as file2:
            json.dump(list1,file2,indent=4)
            p=int(input("parent number:  "))
        for l in list1:
            if l["parent_exercise_id"]==l["id"]:
                print(list1[p-1]["name"])
                p1=list1[p-1]["id"]
        list3=[]
        list4=[]
        new_no1=1
        for x in range(0,len(list2)):
            if list2[x]["parent_exercise_id"]==p1:
                print(" ",new_no1,list2[x]["name"])
                list3.append(list2[x]["name"])
                list4.append(list2[x]["content"])
                new_no1+=1
                
        parent_nevigation1=input("if you want to enter again parent so enter yes/no: ")
        if parent_nevigation1=="yes":
             
            response1=requests.get("https://api.merakilearn.org/courses/"+str(identity)+"/exercises")
            saral1=response1.json()
            with open("course.json","w") as file1:
                json.dump(saral1,file1,indent=4)
                s_no2=1
                list1=[]
                list2=[]
            for j in saral1["course"]["exercises"]:
                if j["parent_exercise_id"]==None:
                    print(s_no2,j["name"])
                    print(" ","1. ",j["slug"])
                    s_no2+=1
                    new_no=1
                    list1.append(j)
                    list2.append(j)
                    continue
                if j["parent_exercise_id"]==j["id"]:
                    print(s_no2,j["name"])
                    s_no2+=1
                    new_no=1
                    list1.append(j)
                for k in saral1["course"]["exercises"]:
                    if j["parent_exercise_id"]!=["id"]:
                        print(" ",new_no,j["name"])
                        new_no+=1
                        list2.append(j)
                        break
            with open("parent.json","w") as file2:
                json.dump(list1,file2,indent=4)
                p=int(input("parent number:  "))
            for l in list1:
                if l["parent_exercise_id"]==l["id"]:
                    print(list1[p-1]["name"])
                    p1=list1[p-1]["id"]
                    break
            list3=[]
            list4=[]
            new_no1=1
            for x in range(0,len(list2)):
                if list2[x]["parent_exercise_id"]==p1:
                    print(" ",new_no1,list2[x]["name"])
                    list3.append(list2[x]["name"])
                    list4.append(list2[x]["content"])
                    new_no1+=1
                               
            choice=int(input("enter your point/options number:  "))
            print(list4[choice-1])
            point_nevigation1=input("if you want to enter again point/options so enter yes/no: ")
            if point_nevigation1=="yes":
                hoice=int(input("enter your point/options number: "))
                print(list4[choice-1])
            else:
                print(list4[choice-1])        
                
        elif parent_nevigation1=="no":
            with open("parent.json","w") as file2:
                json.dump(list1,file2,indent=4)
                for l in list1:
                    if l["parent_exercise_id"]==l["id"]:
                        print(list1[p-1]["name"])
                        p1=list1[p-1]["id"]
                        break
                list3=[]
                list4=[]
                new_no1=1
                for x in range(0,len(list2)):
                    if list2[x]["parent_exercise_id"]==p1:
                        print(" ",new_no1,list2[x]["name"])
                        list3.append(list2[x]["name"])
                        list4.append(list2[x]["content"])
                        new_no1+=1
                        
                choice=int(input("enter your point/options number: "))
                print(list4[choice-1])
                n2=input("if you want to enter again point/options so enter yes/no: ")
                if n2=="yes":
                    hoice=int(input("enter your point/options number: "))
                    print(list4[choice-1])
                else:
                    print(list4[choice-1])
                    
    elif nevigation2=="n":
        response1=requests.get("https://api.merakilearn.org/courses/"+str(identity)+"/exercises")
        saral1=response1.json()
        with open("course.json","w") as file1:
            json.dump(saral1,file1,indent=4)
            s_no2=1
            list1=[]
            list2=[]
        for j in saral1["course"]["exercises"]:
            if j["parent_exercise_id"]==None:
                print(s_no2,j["name"])
                print(" ","1. ",j["slug"])
                s_no2+=1
                new_no=1
                list1.append(j)
                list2.append(j)
                continue
            if j["parent_exercise_id"]==j["id"]:
                print(s_no2,j["name"])
                s_no2+=1
                new_no=1
                list1.append(j)
            for k in saral1["course"]["exercises"]:
                if j["parent_exercise_id"]!=["id"]:
                    print(" ",new_no,j["name"])
                    new_no+=1
                    list2.append(j)
                    break
        with open("parent.json","w") as file2:
            json.dump(list1,file2,indent=4)
            p=int(input("parent number:  "))
        for l in list1:
            if l["parent_exercise_id"]==l["id"]:
                print(list1[p-1]["name"])
                p1=list1[p-1]["id"]
        list3=[]
        list4=[]
        new_no1=1
        for x in range(0,len(list2)):
            if list2[x]["parent_exercise_id"]==p1:
                print(" ",new_no1,list2[x]["name"])
                list3.append(list2[x]["name"])
                list4.append(list2[x]["content"])
                new_no1+=1
                
        n=input("if you want to enter again parent so enter yes/no:   ")
        if n=="yes":
              
            response1=requests.get("https://api.merakilearn.org/courses/"+str(identity)+"/exercises")
            saral1=response1.json()
            with open("course.json","w") as file1:
                json.dump(saral1,file1,indent=4)
                s_no2=1
                list1=[]
                list2=[]
            for j in saral1["course"]["exercises"]:
                if j["parent_exercise_id"]==None:
                    print(s_no2,j["name"])
                    print(" ","1. ",j["slug"])
                    s_no2+=1
                    new_no=1
                    list1.append(j)
                    list2.append(j)
                    continue
                if j["parent_exercise_id"]==j["id"]:
                    print(s_no2,j["name"])
                    s_no2+=1
                    new_no=1
                    list1.append(j)
                for k in saral1["course"]["exercises"]:
                    if j["parent_exercise_id"]!=["id"]:
                        print(" ",new_no,j["name"])
                        new_no+=1
                        list2.append(j)
                        break
            with open("parent.json","w") as file2:
                json.dump(list1,file2,indent=4)
                p=int(input("parent number:   "))
            for l in list1:
                if l["parent_exercise_id"]==l["id"]:
                    print(list1[p-1]["name"])
                    p1=list1[p-1]["id"]
                    break
            list3=[]
            list4=[]
            new_no1=1
            for x in range(0,len(list2)):
                if list2[x]["parent_exercise_id"]==p1:
                    print(" ",new_no1,list2[x]["name"])
                    list3.append(list2[x]["name"])
                    list4.append(list2[x]["content"])
                    new_no1+=1
                          
            choice=int(input("enter your point/options number: "))
            print(list4[choice-1])
            point_nevigation2=input("if you want to enter again point/options so enter yes/no: ")
            if point_nevigation2=="yes":
                hoice=int(input("enter your point/options number: "))
                print(list4[choice-1])
            else:
                print(list4[choice-1])
              
        elif n=="no":
            with open("parent.json","w") as file2:
                json.dump(list1,file2,indent=4)
                p=int(input("parent number:  "))
                for l in list1:
                    if l["parent_exercise_id"]==l["id"]:
                        print(list1[p-1]["name"])
                        p1=list1[p-1]["id"]
                        break
                list3=[]
                list4=[]
                new_no1=1
                for x in range(0,len(list2)):
                    if list2[x]["parent_exercise_id"]==p1:
                        print(" ",new_no1,list2[x]["name"])
                        list3.append(list2[x]["name"])
                        list4.append(list2[x]["content"])
                        new_no1+=1
                        
                choice=int(input("enter your point/options number: "))
                print(list4[choice-1])
                n2=input("if you want to enter again point/options so enter yes/no: ")
                if n2=="yes":
                    hoice=int(input("enter your point/options number: "))
                    print(list4[choice-1])
                else:
                    print(list4[choice-1])
elif navigation1=="n":
    response1=requests.get("https://api.merakilearn.org/courses/"+str(identity)+"/exercises")
    saral1=response1.json()
    with open("course.json","w") as file1:
        json.dump(saral1,file1,indent=4)
        s_no2=1
        list1=[]
        list2=[]
    for j in saral1["course"]["exercises"]:
        if j["parent_exercise_id"]==None:
            print(s_no2,j["name"])
            print(" ","1. ",j["slug"])
            s_no2+=1
            new_no=1
            list1.append(j)
            list2.append(j)
            continue
        if j["parent_exercise_id"]==j["id"]:
            print(s_no2,j["name"])
            s_no2+=1
            new_no=1
            list1.append(j)
        for k in saral1["course"]["exercises"]:
            if j["parent_exercise_id"]!=["id"]:
                print(" ",new_no,j["name"])
                new_no+=1
                list2.append(j)
                break
    with open("parent.json","w") as file2:
        json.dump(list1,file2,indent=4)
        p=int(input("parent number:  "))
    for l in list1:
        if l["parent_exercise_id"]==l["id"]:
            print(list1[p-1]["name"])
            p1=list1[p-1]["id"]
    list3=[]
    list4=[]
    new_no1=1
    for x in range(0,len(list2)):
        if list2[x]["parent_exercise_id"]==p1:
            print(" ",new_no1,list2[x]["name"])
            list3.append(list2[x]["name"])
            list4.append(list2[x]["content"])
            new_no1+=1
            
    n=input("if you want to enter again parent so enter yes/no: ")
    if n=="yes":
        
        
        response1=requests.get("https://api.merakilearn.org/courses/"+str(identity)+"/exercises")
        saral1=response1.json()
        with open("course.json","w") as file1:
            json.dump(saral1,file1,indent=4)
            s_no2=1
            list1=[]
            list2=[]
        for j in saral1["course"]["exercises"]:
            if j["parent_exercise_id"]==None:
                print(s_no2,j["name"])
                print(" ","1. ",j["slug"])
                s_no2+=1
                new_no=1
                list1.append(j)
                list2.append(j)
                continue
            if j["parent_exercise_id"]==j["id"]:
                print(s_no2,j["name"])
                s_no2+=1
                new_no=1
                list1.append(j)
            for k in saral1["course"]["exercises"]:
                if j["parent_exercise_id"]!=["id"]:
                    print(" ",new_no,j["name"])
                    new_no+=1
                    list2.append(j)
                    break
        with open("parent.json","w") as file2:
            json.dump(list1,file2,indent=4)
            p=int(input("parent number:  "))
        for l in list1:
            if l["parent_exercise_id"]==l["id"]:
                print(list1[p-1]["name"])
                p1=list1[p-1]["id"]
                break
        list3=[]
        list4=[]
        new_no1=1
        for x in range(0,len(list2)):
            if list2[x]["parent_exercise_id"]==p1:
                print(" ",new_no1,list2[x]["name"])
                list3.append(list2[x]["name"])
                list4.append(list2[x]["content"])
                new_no1+=1
                    
        choice=int(input("enter your point/options number: "))
        print(list4[choice-1])
        n1=input("if you want to enter again point/options so enter yes/no: ")
        if n1=="yes":
            hoice=int(input("enter your point/options number: "))
            print(list4[choice-1])
        else:
            print(list4[choice-1])  
            
    elif n=="no":
        with open("parent.json","w") as file2:
            json.dump(list1,file2,indent=4)
            for l in list1:
                if l["parent_exercise_id"]==l["id"]:
                    print(list1[p-1]["name"])
                    p1=list1[p-1]["id"]
                    break
            list3=[]
            list4=[]
            new_no1=1
            for x in range(0,len(list2)):
                if list2[x]["parent_exercise_id"]==p1:
                    print(" ",new_no1,list2[x]["name"])
                    list3.append(list2[x]["name"])
                    list4.append(list2[x]["content"])
                    new_no1+=1
                    
            choice=int(input("enter your point/options number: "))
            print(list4[choice-1])
            n2=input("if you want to enter again point/options so enter yes/no: ")
            if n2=="yes":
                hoice=int(input("enter your point/options number: "))
                print(list4[choice-1])
            else:
                print(list4[choice-1])        
