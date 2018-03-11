class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        res=0
       # length=len(str)
        count=0
        judge=2
        if len(str)==0:
            return
        if str[0]=='+':
            judge=0
        elif str[0]=='-':
            judge=1
        if judge==0:
            length=len(str)-1
            for i,ch in enumerate(str):
                number=ord(ch)
                if number<=57 and number>=48:
                    count+=1

            if count==length:
                for i,ch in enumerate(str):
                    number=ord(ch)
                    if number<=57 and number>=48:
                        aft=number-48
                        res+=(aft*10**(length-i))
            return res
        elif judge==1:
            length = len(str) - 1
            for i, ch in enumerate(str):
                number = ord(ch)
                if number <= 57 and number >= 48:
                    count += 1

            if count == length:
                for i, ch in enumerate(str):
                    number = ord(ch)
                    if number <= 57 and number >= 48:
                        aft = number - 48
                        res += (aft * 10 ** (length - i ))
            return -res
        elif judge==2:
            length = len(str)
            for i, ch in enumerate(str):
                number = ord(ch)
                if number <= 57 and number >= 48:
                    count += 1

            if count == length:
                for i, ch in enumerate(str):
                    number = ord(ch)
                    if number <= 57 and number >= 48:
                        aft = number - 48
                        res += (aft * 10 ** (length - i-1))
            return res

if __name__=="__main__":
    sol=Solution()
    print(sol.myAtoi(" 010"))
