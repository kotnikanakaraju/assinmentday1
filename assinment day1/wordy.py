import re

def answer(question):
    if re.match(r"what is (-?\d+)\?",question):
        return int(re.match(r"what is (?\d+)\?",question).group(1))
    match=re.match(r"what is (-?\d+) plus (-?\d+)\?",question)
    if match:
        return int(match.group(1))+int(match.group(2))
    match=re.match(r"what is (-?\d+) (plus|minus|multipliedby|divided by)",match.group(1))
    if match:
        num1=int(match.group(1))
        num2=int(match.group(2))
        operate=match.group(2)

        if operate=='plus':
            return num1+num2
        elif operate=='minus':
            return num1-num2
        elif operate=='multipliedby':
            return num1*num2
        elif operate=='divided by':
            if num2==0:
                raise ValueError("division by zero")
            return num1//num2
    match=re.match(r"what is (-?\.+)?",question)
    if match:
        operate=re.findall(r"(-?\d+) (plus|minus|multiplied by|divided by)",match.group(1))
        
        if not operate:
            raise ValueError("syntyax error")
        
        result=int(operate[0][0])
        for i in range(1,len(operate)):
            num=int(operate[i][0])
            op=operate[i-1][1]
            if op=='plus':
                result+=num
            elif op=='minus':
                result-=num
            elif op=='multipliedby':
                result*=num
            elif op=='divided by':
                if num==0:
                    raise ValueError("division by zero")
                result//=num
        return result
    raise ValueError("syntyax error")

try:
    print(answer("what is 3 plus 5?"))

except ValueError as e:
    print(e)