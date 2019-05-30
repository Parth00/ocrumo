from CompareVersion import CompareVersion

#Input the strings using space to separate them. Eg: 1.34.45.23.34 1.34.65.34.65.76
s1,s2 = raw_input().split()
#Initializing the class
test = CompareVersion()
#Comparing the string versions and printing out the results
if test.compare_version(s1,s2) == 0:
    print("{} is same version as {}".format(s1,s2))
elif test.compare_version(s1,s2) == 1:
    print("{} is greater version than {}".format(s1,s2))
elif test.compare_version(s1,s2) == -1:
    print("{} is greater version than {}".format(s2,s1))
