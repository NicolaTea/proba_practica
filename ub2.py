class BinaryNumber:
    def __init__(self,binary_str):
        self.binary_list=[int(bit) for bit in binary_str]



    def sum(self,other,return_list):
        maxim=max(len(self.binary_list),len(other.binary_list))
        self.binary_list=[0]*(maxim-len(self.binary_list))+self.binary_list
        other.binary_list=[0]*(maxim-len(other.binary_list))+other.binary_list
        new_result=[]


        cf=0
        for i in range(maxim-1,-1,-1):
            sum=self.binary_list[i]+other.binary_list[i]+cf
            new_result.insert(0,sum%2)
            cf=sum//2
        if cf:
            new_result.insert(0,cf)

        if return_list:
            return new_result
        else:
            return ','.join(map(str,new_result))



binary_number1 = BinaryNumber("101")  #5
binary_number2 = BinaryNumber("1110")  #14
binary_number3=BinaryNumber('111')
res_sum1 = binary_number1.sum(binary_number2, return_list=False)
res_sum2 = binary_number1.sum(binary_number2, return_list=True)
print(res_sum1)
print(res_sum2)


class RepoBinaryNumber:
    def __init__(self):
        self.numbers=[]

    def add(self,number):
        self.numbers.append(number)

    def sum_all(self):
        if len(self.numbers)==1:
            num1=self.numbers[0]
            return BinaryNumber.sum(BinaryNumber('0'),num1,False)
        elif len(self.numbers)==2:
            num1=self.numbers[0]
            num2=self.numbers[1]
            return BinaryNumber.sum(num1, num2, False)


repo_binary_number = RepoBinaryNumber()
repo_binary_number.add(binary_number1)
repo_binary_number.add(binary_number2)
# repo_binary_number.add(binary_number3)
print(repo_binary_number.sum_all())