#!/usr/bin/env python
# coding: utf-8

# In[ ]:


tb = float(input("Masukan Tinggi Badan Anda : "))
bb = int(input("Masukan Berat Badan Anda : "))
bmi = bb / (tb**2)
if bmi > 30:
    print ("BMI : Obesitas / Severely Overweight")
elif bmi >= 25 and bmi < 29.9:
    print ("BMI : Gemuk / Overweight")
elif bmi >= 18.5 and bmi < 24.9:
    print ("BMI : Ideal / Healthy")
else:
    print ("BMI : Kurus / Underweight")

