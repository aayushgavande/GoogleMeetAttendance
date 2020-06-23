#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd 
import re


# Using Regular Expression To Identify The Roll Number 

# In[2]:


regex = re.compile('(TC\s+\d{3}?)|(TC\d{3}?)|(TC-\d{3})',re.IGNORECASE)


# In[19]:


# Reading the Chat File replace the 'lecture.txt' with the file name
#make sure the file is in the same folder as this script or enter the whole path for the file

text = ""
for words in open('ChatFile.txt'):
    text += words


# In[4]:


#The text from the file as a string 
text


# In[5]:


#getting the roll number using the regular expression 

roll = regex.findall(text)


# In[20]:


#list of roll numbers found from the text
roll


# In[7]:


#Loading the rollcall list using pandas 

Attendance_df = pd.read_csv('Roll_List.csv')


# In[8]:


Attendance_df


# In[9]:


#Adding a new columns attendance and adding everyone as absent

Attendance_df['Attendance'] = 'Absent'
Attendance_df


# In[10]:


for i in range(0,len(roll)):
    for j in range(0,len(Attendance_df)):
        if(Attendance_df['Roll No.'][j] == roll[i][1] or Attendance_df['Roll No.'][j] == roll[i][0].replace(" ","") or Attendance_df['Roll No.'][j] == roll[i][2].replace("-","")):
            Attendance_df['Attendance'][j] = "Present"


# In[14]:


# Looking at the attendance sheet 
Attendance_df.head(50)


# In[21]:


Attendance_df['Attendance'].value_counts()


# In[22]:


Attendance_df.to_csv('Attendance.csv',index=False) # Saving it to a file named attendance.csv

