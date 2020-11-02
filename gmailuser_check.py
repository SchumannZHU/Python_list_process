import csv
import pandas as pd
from lxml import etree

readpath ='F:\\20gmailcheck\\form.csv'
writepath ='F:\\20gmailcheck\\form2.csv'
resultpath='F:\\20gmailcheck\\result.csv'

#f is the original google-form data may including the typing errors ,but in f2 this problem is fixed. 
'''the field of f is as follows   
タイムスタンプ
学籍番号を教えてください。（半角英数字,例: 2011001, 20M1101）
学籍番号をもう一度入力してください。（半角英数字,例: 2011001, 20M1101）
氏名を教えてください。（例:目白太郎＊スペースなしで入力してください）
所属学科を教えてください。'''

f = open(readpath,'r',encoding='utf_8_sig',newline="")
f2= open(writepath,'w',encoding='utf_8_sig',newline="")
csvread=csv.reader(f, delimiter=',')
csvwrite = csv.writer(f2)
for row in csvread:
    if row[1]==row[2] and len(row[1])==7:
        csvwrite.writerow([row[1],row[3].replace("　","")])
    else:
    #print the data which include typing error 
        print(row)
f.close()
f2.close()

rout="F:/20gmailcheck/view.html"
op=open(rout,encoding="utf-8")
file=op.read()
file2=file.replace("\u3000","")
finder=etree.HTML(file2)
td=finder.xpath("//tr/td/text()")

#create a dict like {ID:name}
sid=list()
sname=list()
for i in range(3,len(td),13):
    sid.append(td[i][2:])
for i in range(5,len(td),13):
    sname.append(td[i])
idname=dict(zip(sid,sname))

#use id to match the 2 file to find the user who is not submit the google-form and save the list in a csv file named f4
f3= open(writepath,'r',encoding='utf_8_sig',newline="")
f4= open(resultpath,'w',encoding='utf_8_sig',newline="")
csvwrite4 = csv.writer(f4)
df = pd.read_csv(f3,header=None,usecols=[0])
idlist = list(df[0])
for i in sid:
    if i not in idlist:
        csvwrite4.writerow([i,idname[i]])   
    else:
        print(i,"is OK")
f3.close()
f4.close()
