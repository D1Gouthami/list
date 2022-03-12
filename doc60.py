print("hello everyone")
print("_welcome to KBC_")
print("* very good luck for your game***")
print("so lets play the game")
question_list=["what is the capital of India?","How many colours in rainbow?",
"How many girls in navgurukul ? ","which course we are doing in navgurukul?"]
options_list=[["bihar","delhi","kolkata","canada"],["8","9","7","10"],["118","120","100","104"],["beaty palour","swimming course","fashion designer","engineering course"]]
life_line=[["delhi","bihar"],["7","10"],["120","118"],["engineering course","beaty palour"]]
solution_list2=[1,1,2,1]
solution_list=[2,3,1,4]
i=0
count=0
while i<len(question_list[i]):
	print("Q.",i+1,question_list[i])
	j=0
	while j<len(options_list[i]):
		print(j+1,options_list[i][j])
		j=j+1
	user=int(input("cho…
def fun(a):
    i=0
    max=0
    while i<len(a):
        if a[i]>max:
            max=a[i]
        i+=1
    print(max)