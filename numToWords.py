def numberToWords(num):
    
        if num== 0:
            return "Zero"
        single = {1:" One",2:" Two",3:" Three",4:" Four",5:" Five",6:" Six",7:" Seven",8:" Eight",9:" Nine"}
        second1 = {10: " Ten",11:" Eleven",12:" Twelve",13:" Thirteen",14:" Fourteen",15:" Fifteen",16:" Sixteen",17:" Seventeen",18:" Eighteen",19:" Nineteen"}
        double = {2:" Twenty",3:" Thirty",4:" Forty",5:" Fifty",6:" Sixty",7:" Seventy",8:" Eighty",9:" Ninety"}
        string = ""
        def inputThrees(num3):
            temp = ""
            if int(num3/100) != 0:
                temp = temp + single[int(num3/100)]+ " Hundred"
            if len(str(num3%100)) == 2 :
                if num3%100 in second1.keys():
                    temp = temp + second1[num3%100]
                elif int((num3%100)/10) in double.keys():
                    temp = temp + double[int((num3%100)/10)]
                    if num3%10 != 0:
                        temp = temp + single[num3%10]
            elif num3%10 != 0:
                temp = temp + single[num3%10]
            return temp
            
        size = len(str(num))
        if size> 9:
            billion = int(num/10**9)
            string = string + inputThrees(billion) + " Billion"
        if size> 6:
            million = int(int(num%10**9)/10**6)
            if million > 0:
                string = string + inputThrees(million) + " Million"
        if size> 3:
            Thousand = int(int(num%10**6)/10**3)
            if Thousand > 0:
                string = string + inputThrees(Thousand)+ " Thousand"
        if size>0 :
            num2 = num%10**3
            string = string + inputThrees(num2)
            
        return string.lstrip()
        