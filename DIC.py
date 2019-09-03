"""
dict = {'Name': 'Bodi', 'Age': 14, 'Class': 'First'}
dict["Google"] = "Larry Page en Sergey Brin"
print ("['Name']: ", dict['Name'])
print ("['Age']: ", dict['Age'])
print ("['Google]: ", dict['Google'])
if "Google" in dict:
    print("Google zit erin!")
del dict["Age"]
if "Age" not in dict:
    print("TurboBUILD IS BACKKKCKCKCKKCKCKC!")
"""
    
dic1={'1':'10', '2':'20'}
dic2={'3':'30', '4':'40'}
dic3={'5':'50', '6':'60'}
def Merge(dic1, dic2):
    return(dic1.update(dic2))
def Merge2(dic1, dic3):
    return(dic1.update(dic3))
print(Merge(dic1, dic2))
print(Merge2(dic1, dic3))
print(dic1)