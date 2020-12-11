import csv
import re
import sys

def convert_to_csv(log_file):
    """Converts NGNX log type access file into CSV, IP address are MD5 encoded"""
    #Reads log file           
    with open(log_file) as f:
            f = f.readlines()
    log_list = []
    #columns names
    col_names=['time','confname', 'meetingId', 'clientURL','comment', 'rating']
    for line in f:
        log_list.append(line)
    #Creates the first line in the csv with the columns names
    with open('log.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(col_names)  

    #Separates lines into fields using the search_pattern based on the previously defined column names col_names
    for x in range(len(log_list)):
        line=[]
        # splits a word into character into the line_separation function and return a list of the lines
        for y in col_names:
            row=search_pattern(y,log_list[x])
            line.append(row)
        with open('log.csv', 'a', newline='') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(line)

def search_pattern(row_name,line):
    self = ""
    #Based on the column name different regex patterns are searched for
    if (row_name == 'time'):
        self = re.search(r'[0-9][0-9][0-9][0-9]\S[0-9][0-9]\S[0-9][0-9]T[0-9][0-9]\S[0-9][0-9]\S[0-9][0-9]\S[0-9][0-9]\S[0-9][0-9]', line)
        if (self != None):
            return self.group()
        else:
            return("not found")
    
    elif (row_name == 'confname'): 
        self = re.search(r'confname\S\w\w\S\S\S\S\w\w[ \w-]*', line)
        if (self != None):
            return re.sub(r'confname\S\w\w\S\S\S\S\w\w',"",self.group())
        else:
            return("not found")
    
    elif (row_name == 'meetingId'): 
        self = re.search(r'meetingId\S\w\w\S\S\S\S\w\w[ \w-]*', line)
        if (self != None):
            return re.sub(r'meetingId\S\w\w\S\S\S\S\w\w',"",self.group())
        else:
            return("not found")
    
    elif (row_name == 'clientURL'): 
        self = re.search(r'clientURL\S\w\w\S\S\S\S\w\w[- .-?=\w]*', line)
        if (self != None):
            return re.sub(r'clientURL\S\w\w\S\S\S\S\w\w',"",self.group())
        else:
            return("not found")
        
    elif (row_name == 'comment'): 
        self = re.search(r'comment\S\w\w\S\S\S\S\w\w[ \w-]*', line)
        if (self != None):
            return re.sub(r'comment\S\w\w\S\S\S\S\w\w',"",self.group())
        else:
            return("not found")
        
    elif (row_name == 'rating'): 
        self = re.search(r'rating\S\w\w\S\S\S', line)
        if (self != None):
            return re.sub(r'rating\S\w\w\S\S',"",self.group())
        else:
            return("not found")

if __name__== "__main__":
    convert_to_csv(str(sys.argv[1]))