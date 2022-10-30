#!/usr/bin/env python
# coding: utf-8

# In[4]:


import string
import random
if __name__ == "__main__":
    s1 = string.ascii_uppercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    s5 = string.ascii_lowercase
    s6 = string.ascii_letters
    s6 = string.hexdigits
    plen = int(input("Enter password length: "))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    s.extend(list(s5))
    s.extend(list(s6))

    print("Your password: ", end="")
    print("".join(random.sample(s, plen)))


# In[ ]:


points = {'A+': 4.0,'A': 3.75,'A-': 3.50,'B+': 3.25,'B': 3.0,'B-': 2.75,'C+': 2.50,'C': 2.25,'D': 2.0,'F': 0.0}
num_courses = 0
total_points = 0
done = False
while not done:
    grade = input()
    if grade =='':
        done = True
    elif grade not in points:
            print("Unknown grade '{0}' being ignored".format(grade))
    else:
                num_courses += 1
                total_points += points[grade]
                if num_courses > 0:
                    print('Your GPA is {0:.3}'.format(total_points / num_courses))

