phrase = "PythonProgramming"
list_p = [] #空のリストを作成
for p in phrase: #繰り返しで位置を文字ずつ検査
     if p not in list_p: # pがlist_pにまだ含まれていなければ
        list_p.append(p) #list_pにpを追加
print (len(phrase) - len(list_p)) #17-11=6つまり重複下文字の数

for p in list_p: #文字を一つ一つ出力
    print(p, end="") #改行をなくす
print () #次の出力ができるように改行だけ出力
print ("".join(list_p)) #他の出力方法
