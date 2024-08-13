
__all__ = ['DIRNAME', 'IN_SOURCE', 'OUT_SOURCE', 'POWER', 'RINT', 'TC_SOURCE', 'generate',
           'compile_them', 'zip_codechef', 'zip_hackerrank', 'zip_hackerearth', 'zip_them',
            'make_dirs', 'Error', 'EmptyFileException', 'CompilationError',
           'RunError', 'ValueOutsideRange']

import math
import os
import random
import shutil
import sys
import subprocess
from string_generator import string_gen




class Error(Exception):
    """Base class for other exceptions."""
    pass

class EmptyFileException(Error):
    """Raised when output file is empty"""
    pass

class CompilationError(Error):
    """Raised when logic program is not compiled properly"""
    pass

class RunError(Error):
    """Raised when logic program encounters runtime error"""
    pass

class ValueOutsideRange(Error):
    """Raised when value entered is outside range"""
    pass



DIRNAME = os.path.abspath(os.path.dirname(__file__)) # Absolute path of the file
IN_SOURCE = os.path.join(DIRNAME, 'input')
OUT_SOURCE = os.path.join(DIRNAME, 'output')
TC_SOURCE = os.path.join(DIRNAME, 'test-cases')
TC_ZIP = TC_SOURCE + '.zip'
POWER = math.pow
RINT = random.randint
WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'



def make_dirs():
    """Deletes old directories and creates new ones."""

    shutil.rmtree(IN_SOURCE, ignore_errors=True)
    shutil.rmtree(OUT_SOURCE, ignore_errors=True)
    shutil.rmtree(TC_SOURCE, ignore_errors=True)
    try:
        os.remove(TC_ZIP)
    except OSError:
        pass

    os.mkdir(IN_SOURCE)
    os.mkdir(OUT_SOURCE)



def main():
 
    make_dirs()

    test_files = 50  # number of test files, change it according to you.
    in_file = os.path.join(IN_SOURCE, f'inputfile.txt')
    import random
    sout=set()


    from collections import OrderedDict

    def write_roman(num):

        roman = OrderedDict()
        roman[1000] = "M"
        roman[900] = "CM"
        roman[500] = "D"
        roman[400] = "CD"
        roman[100] = "C"
        roman[90] = "XC"
        roman[50] = "L"
        roman[40] = "XL"
        roman[10] = "X"
        roman[9] = "IX"
        roman[5] = "V"
        roman[4] = "IV"
        roman[1] = "I"

        def roman_num(num):
            for r in roman.keys():
                x, y = divmod(num, r)
                yield roman[r] * x
                num -= (r * x)
                if num <= 0:
                    break

        return "".join([a for a in roman_num(num)])
    

    def returnGet(num):
        return f"GET {num}"
    
    def returnSet(num1,num2):
        return f"SET {num1} {num2}"


    
    from collections import deque
    # Definition for a binary tree node.
    class TreeNode():
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    class Heap():
        def heapify(self,arr,N,i):
            largest = i  
            l = 2 * i + 1  
            r = 2 * i + 2  
        
            
            if l < N and arr[l] > arr[largest]:
                largest = l
        
            
            if r < N and arr[r] > arr[largest]:
                largest = r
        
            
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
        
                self.heapify(arr, N, largest)


        def generateMaxHeapUsingSortedArray(self,nums):
            nums=nums[::-1]
            
            startIdx = len(nums) // 2 - 1
 
    
            for i in range(startIdx, -1, -1):
                self.heapify(nums, len(nums), i)

            return nums
        
        

    class Solution():

        def sortedArrayToBST(self, nums):
            if not nums:
                return None
            mid=len(nums)//2
            root=TreeNode(nums[mid])
            root.left=self.sortedArrayToBST(nums[:mid])
            root.right=self.sortedArrayToBST(nums[mid+1:])
            return root
        
        def bfs(self,bst):
            ans=[]
            if bst is None:
                return
            queue = [bst]

            while len(queue) > 0:
                
                cur_node = queue.pop(0)
                while cur_node=="N" and len(queue)>0:
                    cur_node = queue.pop(0)
                    ans.append("N")
                if cur_node!="N":
                    ans.append(cur_node.val)
                else:
                    break
                if cur_node.left is not None:
                    queue.append(cur_node.left)
                else:
                    queue.append("N")

                if cur_node.right is not None:
                    queue.append(cur_node.right)
                else:
                    queue.append("N")

            j=len(ans)-1
            
            while j>=0:
                if ans[j]=="N":
                    ans.pop(-1)
                    j-=1
                else:
                    break

            return ans

        def printBST(self, root):
            queue = deque([(root, 0)])
            nodes = []
            while queue:
                currentNode, currentLevel = queue.popleft()
                if len(nodes) == currentLevel:
                    nodes.append([currentNode.val])
                else:
                    nodes[currentLevel].append(currentNode.val)

                if currentNode.left is not None:
                    queue.append((currentNode.left, currentLevel+1))
                if currentNode.right is not None:
                    queue.append((currentNode.right, currentLevel+1))
            return nodes
        

        def inOrderTraversal(self,node):
            ans=[]

            def inOrderTraversalutil(node):
                if node==None:
                    return
                if node.left!=None:
                    inOrderTraversalutil(node.left)
                
                ans.append(node.val)

                if node.right!=None:
                    inOrderTraversalutil(node.right)
            
            inOrderTraversalutil(node)
            
            return ans
        

        
        
            

  
    # def shuffle_string(s):
    #     # Convert the string into a list of characters
    #     char_list = list(s)
    #     # Shuffle the list
    #     random.shuffle(char_list)
    #     # Join the shuffled list back into a string
    #     shuffled_string = ''.join(char_list)
    #     return shuffled_string
    
    # seti=set()
    brac=["[]","{}","()","[]","{}","()"]
    for i in range(0, test_files + 1):
        s=set()
        print(f'Generating input: {i}')
        sys.stdout = open(in_file, 'a')

        # Input area will start here,
        # everything that you print out here will be taken as input in your logic file.

        # Input File Printing Starts
        # number of test cases in (1,10^5)
        # required_input = RINT(1, POWER(10, (i // 2) + 1))


        # #===================================== string cases =============================================#


        # required_input = RINT(1, 40)
        # # print(required_input)
        # # # # r=RINT(1,50)
        # # # # c=RINT(1,50)
        # s1=(string_gen.random_string(required_input,alpha=True))
        
        # print(s1.lower())    

        # for i in range(required_input):
            
        #     if i<required_input-1:
        #         print(s1,end=" ")
        #     else:
        #         print(s1)

        # print(r,c)

        # for i in range(r):
        #     for j in range(c):
        #         s1=(string_gen.random_string(length=RINT(1,1),alpha=True))
            
        #         if j<c-1:
        #             print(s1,end=" ")
        #         else:
        #             print(s1)
        
        
        # #======================================================== Number Case ============================================================#

        # required_input = RINT(1, 10000)
        # another = RINT(1, 1000)
        # print(required_input)
        # # another1=RINT(another,math.floor(math.log2(required_input)))
        # # s1=(string_gen.random_string(required_input,alpha=True))
        # # print(s1.upper())
        # # s1=(string_gen.random_string(another,alpha=True))
        # # print(s1.upper())

        # while (required_input) in sout:
        #     required_input = RINT(1, 100000)
        
        # sout.add(required_input)

        # print(required_input)
        # # print(another)




        # #======================================================== array Case ============================================================#


        required_input = RINT(1,500)
        print(required_input)
        array=[]
        last=0
        for j in range(1,required_input+1):
            if last==1:
                array.append(1)
            else:
                array.append(0)
                if RINT(1,10)==1:
                    last=1
            # array.append(num)
    
        # array.sort()
        # rn=RINT(1,required_input)
        # array=array[rn:]+array[:rn]
        print(" ".join(map(str,array)))
        # print(another)
        # s.clear()

        # print()
              

        # #======================================================== Square Matrix Case ============================================================#

        # required_input = RINT(1,5)
        # another =RINT(1,5)
        # print(required_input,another)

        # for i in range(required_input):
        #     for j in range(another):
        #         # choice=RINT(0,5)
        #         number=RINT(1,50)
        #         # if i==j:
        #         #     number=0
        #         # if choice >4:
        #         #     number=0
        #         if j==another-1:
        #             print(number)
        #         else:
        #             print(number,end=" ")
        # print(RINT(1,50))
        # print()



        # #======================================================== Heap Case ============================================================#

        # N = RINT(1,250)
        # M= RINT(1,250)
        # print(N,M)

        # a=Heap()
        
        # array=[]

        # for i in range(N):
        #     num=RINT(1,250)
        #     while num in s:
        #         num=RINT(1,250)
        #     s.add(num)
        #     array.append(num)
        
        # hp=a.generateMaxHeapUsingSortedArray(array)

        # print(" ".join(map(str,hp)))
        # s.clear()
        
        # array=[]
        # for i in range(M):
        #     num=RINT(1,250)
        #     while num in s:
        #         num=RINT(1,250)
        #     s.add(num)
        #     array.append(num)
        
        # hp=a.generateMaxHeapUsingSortedArray(array)

        # print(" ".join(map(str,hp)))
        # s.clear()

        # #======================================================== graph Case ============================================================#

        # n = RINT(1, 50)
        # m = RINT(n, math.floor(n*2))
        
        # print(n,m)

        # for i in range(m):
            
        #     edge=(RINT(0,n-1),RINT(0,n-1))

        #     while edge in s:
        #         edge=(RINT(0,n-1),RINT(0,n-1))
            
        #     s.add(edge)


        #     print(edge[0],edge[1])            

        # # print(RINT(0,n-1))
        # print()
        # s.clear()

        # #=========================================================== CBST cases ==========================================================#

        # required_input = RINT(1, 500)
        
        # array=[]    
        # for i in range(required_input):

        #     number=RINT(1,500)
        #     while number in s:
        #         number=RINT(1,500)
        #     s.add(number)
        #     array.append(number)
    
        
        # tree=Solution()

        # array.sort()

        # a=tree.sortedArrayToBST(array)
        
        # final=tree.bfs(a)
        

        # print(" ".join(map(str,final)))        
        # k=RINT(1,500)
        # while k in s:
        #     k=RINT(1,500)
        # print(k)

     
        # s.clear()

        # #=========================================================== tree cases ==========================================================#

        # required_input = RINT(1, 500)
        # array=[]
        # for i in range(required_input):

        #     number=RINT(1,500)
        #     while number in s:
        #         number=RINT(1,500)
        #     choice=RINT(1,15)
        #     if choice==1 and i>3:
        #         number="N"
        #     else:
        #         s.add(number)
        #     array.append(number)
    
        # print(" ".join(map(str,array)))        
        
        





        # Input File Printing Ends
        sys.stdout = sys.__stdout__




if __name__ == "__main__":
    
    main()
