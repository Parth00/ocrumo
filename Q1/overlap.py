#Function to check whether 2 lines overlap or not
def check_overlap(x1,x2,x3,x4):
    #When 2 lines overlap, one of them or both co-ordinates of any line is in between the two co-ordinates of other line
    #Returns true if overlaps else false
    return (x3>=x1 and x3<=x2) or (x1>=x3 and x1<=x4) or (x1>=x4 and x1<=x2)


#Enter 4 digits at once using space Line 1 (x1, x2) Line 2 (x3, x4)
x1,x2,x3,x4 = map(int, raw_input().split())


#Assigning value to ans. 'Overlaps' if check_overlap returns true and 'Doesn\'t Overlap' if false
ans = 'Overlaps' if check_overlap(x1,x2,x3,x4)==True else 'Doesn\'t Overlap'


#Printing the ans
print(ans)

#Object oriented style below:

# class Lines:
#     def __init__(self, x1, x2, x3, x4):
#         self.x1 = x1
#         self.x2 = x2
#         self.x3 = x3
#         self.x4 = x4

#     def check_overlap(self):
#         return (self.x3 >= self.x1 and self.x3 <= self.x2) or (self.x1 >= self.x3 and self.x1 <= self.x4) or (self.x1 >= self.x4 and self.x1 <= self.x2)

# if __name__ == '__main__':
#     x1,x2,x3,x4 = map(int, raw_input().split())
#     l = Lines(x1,x2,x3,x4)
#     result = 'Overlaps' if l.check_overlap()==True else 'Doesn\'t Overlap'
#     print(result)