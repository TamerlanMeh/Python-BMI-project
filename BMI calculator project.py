#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# BMI Calculator


# In[25]:


#BMI = (weight) / (height  * height )

#This will be the equation that is used to calculate BMI


# In[32]:


name =str(input("Enter your name please "))

weight = int(input("Enter your weight in kg "))


height = float(input("Enter your weight in m "))


BMI = (weight) / (height  * height )

print(BMI)


if 12 >= BMI >= 186:
    print(name + ", "+ "Enter a valid height and a valid weight")
elif BMI <= 16:
    print(name + ", "+ "you are severly underweight")
elif BMI <= 18.4:
    print(name + ", "+ 'you are underweight')
elif 18.5 <= BMI <= 24.9:
    print(name + ", " + "you are normal")
elif 25 <= BMI <= 39.9:
    print(name + ", " + "you are overweight")
elif BMI >= 40:
    print(name + ", "+ "you are obese")

    

