def above75(studentDict):

    for i in studentDict:
        marks = studentDict[i]["Marks"]
        if marks > 75:
            print("Name : ", studentDict[i]["Name"], "\nMarks : ", studentDict[i]["Marks"],"\n")


#Driver's Code
studentDict =  {    "RollNo : 1"  : {"Name" : "Rounik", 
                                    "Marks" : 80},

                    "RollNo : 2"  : {"Name" : "Ayan"  , 
                                    "Marks" : 79},

                    "RollNo : 30" : {"Name" : "Vinay" , 
                                    "Marks" : 75},
                                    
                    "RollNo : 40" : {"Name" : "Raju"  , 
                                    "Marks" : 50}
                }

print("Student Scoring Above 75 are\n")
above75(studentDict)
