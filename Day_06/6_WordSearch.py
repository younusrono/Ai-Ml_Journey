data=True
line=1
word="python"
with open("Day_6/6_sample.txt","r") as f:
    while data :
        data=f.readline()
        if("python" in data):
            print(f"{word} Found at line {line}")
            break
        print(data)
        line+=1
