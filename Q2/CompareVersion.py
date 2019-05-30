class CompareVersion():
    
    def compare_version(self, s1, s2):
        v1 = s1.split(".")
        v2 = s2.split(".")
        i = 0
        v1_len,v2_len = len(v1),len(v2)
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
        
        while i < len(v1):
            if int(v2[i]) > int(v1[i]):
                return -1
            if int(v1[i]) > int(v2[i]):
                return 1
            i += 1
        return 0
            
        