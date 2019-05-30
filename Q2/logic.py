from CompareVersion import CompareVersion

s1,s2 = raw_input().split()
test = CompareVersion()
if test.compare_version(s1,s2) == 0:
    print("{} is same version as {}".format(s1,s2))
elif test.compare_version(s1,s2) == 1:
    print("{} is greater version than {}".format(s1,s2))
elif test.compare_version(s1,s2) == -1:
    print("{} is greater version than {}".format(s2,s1))