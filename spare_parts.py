import pandas as pd
import numpy as np
import os
SIZE_LIMIT =  5000000 # this bumber is in bytes
def add_thought(thoughts):
    count = int(open("counter.txt", "r").readlines()[0])
    # adding main logic
    number_bytes = os.path.getsize("{}.csv".format(count))
    if(number_bytes < SIZE_LIMIT):
        dataframe = pd.read_csv("{}.csv".format(count))
        dataframe = pd.concat([dataframe,pd.DataFrame([thoughts], columns =['blog'])],axis = 0)
        # editing
        x = list(dataframe.columns )
        x.pop()
        dataframe.drop(x, axis =1, inplace = True)
        dataframe.to_csv("{}.csv".format(count))
        return dataframe
    else:
        # appending counter
        file = open("counter.txt", "w")
        file.write(str(count+1))
        file.close()
        # creating new dataframe
        dataframe = pd.DataFrame([thoughts], columns =['blog'])
        x = list(dataframe.columns)
        x.pop()
        dataframe.drop(x, axis =1, inplace = True)
        dataframe.to_csv("{}.csv".format(count+1))
        return dataframe

def get_blogs():
    counter = int(open("counter.txt", "r").readlines()[0])
    final_list = []
    for i in range(counter):
        dataframe = pd.read_csv("{}.csv".format(i+1))
        for i in list(dataframe['blog']):
            print(i)
            i = i.replace("\r\n","1-1")
            final_list.append(i)
    return final_list
def get_projects():
    counter = int(open("counter_2.txt", "r").readlines()[0])
    final_list = []
    for i in range(counter):
        dataframe = pd.read_csv("project{}.csv".format(i+1))
        dataframe = dataframe.to_numpy()
        for i in dataframe:
            i[1] = i[1].replace("\r\n","1-1")
            #i[1] = i[].replace("\r\n","1-1")
            final_list.append(i)
    return final_list


# ddeleting and modification function



#-------------------------------------[PROJECT AREA]-----------------------------------------------------------
def add_project(description,project_name,image_link, project_link):
    count = int(open("counter_2.txt", "r").readlines()[0])
    # adding main logic
    number_bytes = os.path.getsize("project{}.csv".format(count))
    if(number_bytes < SIZE_LIMIT):
        dataframe = pd.read_csv("project{}.csv".format(count))
        dataframe = pd.concat([dataframe,pd.DataFrame([[description,project_name,image_link, project_link]],
                                                       columns =['description','project_name','image_link', 'project_link'])],
                                                     axis = 0,ignore_index=True)
        # editing
        print(dataframe)
        x = list(dataframe.columns)
        for i in range(4):
            x.pop()
        dataframe.drop(x, axis =1, inplace = True)
        dataframe.to_csv("project{}.csv".format(count))
        return dataframe
    else:
        # appending counter
        file = open("counter_2.txt", "w")
        file.write(str(count+1))
        file.close()
        # creating new dataframe
        dataframe = pd.DataFrame([[description,project_name,image_link, project_link]], 
                                 columns =['description','project_name','image_link', 'project_link'],
                                   axis = 0, ignore_index = True)
        print(dataframe)
        x = list(dataframe.columns)
        for i in range(4):
            x.pop()
        dataframe.drop(x, axis =1, inplace = True)
        dataframe.to_csv("project{}.csv".format(count+1))
        return dataframe