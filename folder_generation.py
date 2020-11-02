from lxml import etree
rout=input("ダウンロードしたファイルのルートを記入してください。（例：C:\\Users\\jasmi\\Desktop\\view.html）")
op=open(rout,encoding="utf-8")
file=op.read()


file2=file.replace("\u3000"," ")
finder=etree.HTML(file2)
td=finder.xpath("//tr/td/text()")
lenth = len(td)
cols = lenth//14
newlist = [[0 for i in range(14)] for j in range(cols)]
for i in range(len(td)):
    newlist[i//14][i%14]=td[i]

gakka=input("学科は？(例：製菓学科,心理ｶｳﾝｾﾘﾝｸﾞ学科,ﾋﾞｼﾞﾈｽ社会学科)")
dic = {'看護学科':'Nr', '理学療法学科':'Py',"言語聴覚学科":"Se","作業療法学科":"Oc",
      "心理ｶｳﾝｾﾘﾝｸﾞ学科":"Ps","人間福祉学科":"Ht","子ども学科":"Ud","児童教育学科":"Ce",
      "社会情報学科":"Sl","メディア学科":"Ma","地域社会学科":"Lc","経営学科":"Bi","英米語学科":"Eg",
      "中国語学科":"Cn","韓国語学科":"Kr","日本語・日本語教育学科":"Jp","製菓学科":"Pt",
      "生活科学科":"Si","ﾋﾞｼﾞﾈｽ社会学科":"Bs","歯科衛生学科":"Dn",}
drive = dic[gakka]

nen=input("学籍番号年度は？(例：2020)")
import csv
path =input('保存先のフォルダーとファイル名のルートを記入してください(例: F:\\IDfolder\\Pt.csv)')
path2=input("どのドライブにフォルダーを作成する予定ですか。本番の場合はDを記入してください、テスト環境ではFなどご自由に（例：D）")

f = open(path,'w',encoding='utf_8_sig',newline="")
csv_write = csv.writer(f)
for row in newlist:
    if row[4]==gakka and row[3][0:4]==nen:
        std=row[3][2:]
        group=row[8][0]
        # 短期大学のルートが違う
        if gakka=="製菓学科" or gakka=="生活科学科" or gakka=="ﾋﾞｼﾞﾈｽ社会学科" or gakka=="歯科衛生学科" :
            pa= path2 + ':\\Col\\' + drive+ '\\'+nen+ '\\' + group + '\\' + std
        else:
            pa= path2 + ':\\Uni\\' + drive+ '\\'+nen+ '\\' + group + '\\' + std
        csv_write.writerow([std,pa,group,nen])
f.close()
input("完了します。")
