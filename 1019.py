time= int(input())
hours = time // 3600
time= time % 3600
minutes = time // 60
time= time % 60
seconds = time 
print (hours,":",minutes,":",seconds, sep="") #sep is used for removing extra spaces otherwise in the answer presentation error will come