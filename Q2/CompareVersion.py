class CompareVersion():
    
    """ Class to implement comparision of two string versions"""
    
    def compare_version(self, s1, s2):
        #Spliting both the strings from the delimeters
        v1 = s1.split(".") 
        v2 = s2.split(".")
        i = 0
        #Finding length of each version string (excluding . )
        v1_len,v2_len = len(v1),len(v2)
        #Normalizing the sizes of both the string versions if they do not match
        if v1_len > v2_len:
            len_diff = v1_len - v2_len
            while len_diff != 0:
                v2.append('0')
                len_diff -= 1
        else:
            len_diff = v2_len - v1_len
            while len_diff != 0:
                v1.append('0')
                len_diff -= 1
        #Comparing each string in the version 1 array with version 2 array after converting into integer
        while i < len(v1):
            if int(v2[i]) > int(v1[i]):
                #Version 2 is greater
                return -1
            if int(v1[i]) > int(v2[i]):
                #Version 1 is greater
                return 1
            i += 1
        #Both versions are same
        return 0
            
        
