from flask import Flask, render_template
import json

app = Flask(__name__)




s='{"nowonair_list":{"g1":{"previous":{"id":"2023051118707","event_id":"18707","start_time":"2023-05-11T16:10:00+09:00","end_time":"2023-05-11T16:15:00+09:00","area":{"id":"130","name":"東京"},"service":{"id":"g1","name":"ＮＨＫ総合１","logo_s":{"url":"//www.nhk.or.jp/common/img/media/gtv-100x50.png","width":"100","height":"50"},"logo_m":{"url":"//www.nhk.or.jp/common/img/media/gtv-200x100.png","width":"200","height":"100"},"logo_l":{"url":"//www.nhk.or.jp/common/img/media/gtv-200x200.png","width":"200","height":"200"}},"title":"きょうの料理ビギナーズ （５）ご飯のおとも カレー鶏そぼろ","subtitle":"つくりおきができる便利な「ご飯のおとも」は、ひとりごはんの強い味方です。カレー風味が食欲をそそる「カレー鶏そぼろ」、トロッとした「塩こぶなめたけ」を紹介します","genres":["0205","1015"]},"present":{"id":"2023051121675","event_id":"21675","start_time":"2023-05-11T16:15:00+09:00","end_time":"2023-05-11T17:00:00+09:00","area":{"id":"130","name":"東京"},"service":{"id":"g1","name":"ＮＨＫ総合１","logo_s":{"url":"//www.nhk.or.jp/common/img/media/gtv-100x50.png","width":"100","height":"50"},"logo_m":{"url":"//www.nhk.or.jp/common/img/media/gtv-200x100.png","width":"200","height":"100"},"logo_l":{"url":"//www.nhk.or.jp/common/img/media/gtv-200x200.png","width":"200","height":"200"}},"title":"あしたが変わるトリセツショー 正しい保湿術！冬の乾燥に負けないかゆみ撃退法","subtitle":"乾燥肌によるかゆみにお悩みのあなたへ、ＭＣ石原さとみが“正しい保湿術”をお届け！皮膚科医推薦！お肌に浸透し水分量をアップさせる保湿剤の塗り方「３Ｔ塗り」とは？","genres":["0515","0203","0205"]},"following":{"id":"2023051118710","event_id":"18710","start_time":"2023-05-11T17:00:00+09:00","end_time":"2023-05-11T18:00:00+09:00","area":{"id":"130","name":"東京"},"service":{"id":"g1","name":"ＮＨＫ総合１","logo_s":{"url":"//www.nhk.or.jp/common/img/media/gtv-100x50.png","width":"100","height":"50"},"logo_m":{"url":"//www.nhk.or.jp/common/img/media/gtv-200x100.png","width":"200","height":"100"},"logo_l":{"url":"//www.nhk.or.jp/common/img/media/gtv-200x200.png","width":"200","height":"200"}},"title":"ニュースＬＩＶＥ！ゆう５時「相撲部」があります","subtitle":"▽令和初「春の園遊会」車いすテニス国枝慎吾さんら招待 ▽大谷翔平選手の「ホームランかぶと」すべて手作業の工房 ▽大相撲夏場所へ「北青鵬」に注目 ＃君の声","genres":["0000","0202","0205"]}}}}'
#print(s)
k = '[{"publishingOffice":"福岡管区気象台","reportDatetime":"2023-05-19T11:00:00+09:00","timeSeries":[{"timeDefines":["2023-05-19T11:00:00+09:00","2023-05-20T00:00:00+09:00","2023-05-21T00:00:00+09:00"],"areas":[{"area":{"name":"福岡地方","code":"400010"},"weatherCodes":["200","211","101"],"weathers":["くもり　所により　雨","くもり　夕方　から　晴れ","晴れ　時々　くもり"],"winds":["北の風　海上　では　北東の風　やや強く","北の風　海上　では　はじめ　北東の風　やや強く","北西の風"],"waves":["２メートル","２メートル　後　１メートル","１メートル"]},{"area":{"name":"北九州地方","code":"400020"},"weatherCodes":["200","211","101"],"weathers":["くもり　所により　雨","くもり　夕方　から　晴れ","晴れ　時々　くもり"],"winds":["東の風　後　北の風　海上　では　北東の風　やや強く","北の風　北九州・遠賀地区　では　はじめ　北東の風　やや強く","西の風"],"waves":["２メートル　ただし　瀬戸内側　では　１メートル　後　０．５メートル","２メートル　後　１メートル　ただし　瀬戸内側　では　０．５メートル","１メートル　ただし　瀬戸内側　では　０．５メートル"]},{"area":{"name":"筑豊地方","code":"400030"},"weatherCodes":["200","211","101"],"weathers":["くもり　所により　雨","くもり　夕方　から　晴れ","晴れ　時々　くもり"],"winds":["東の風　後　北の風","北の風","西の風"]},{"area":{"name":"筑後地方","code":"400040"},"weatherCodes":["200","211","101"],"weathers":["くもり　所により　雨","くもり　昼過ぎ　から　晴れ","晴れ　時々　くもり"],"winds":["北東の風　後　北の風","北の風","西の風"],"waves":["０．５メートル","０．５メートル","０．５メートル"]}]},{"timeDefines":["2023-05-19T12:00:00+09:00","2023-05-19T18:00:00+09:00","2023-05-20T00:00:00+09:00","2023-05-20T06:00:00+09:00","2023-05-20T12:00:00+09:00","2023-05-20T18:00:00+09:00"],"areas":[{"area":{"name":"福岡地方","code":"400010"},"pops":["30","20","10","10","0","0"]},{"area":{"name":"北九州地方","code":"400020"},"pops":["20","20","10","10","0","0"]},{"area":{"name":"筑豊地方","code":"400030"},"pops":["20","20","10","0","0","0"]},{"area":{"name":"筑後地方","code":"400040"},"pops":["30","10","10","0","0","0"]}]},{"timeDefines":["2023-05-19T09:00:00+09:00","2023-05-19T00:00:00+09:00","2023-05-20T00:00:00+09:00","2023-05-20T09:00:00+09:00"],"areas":[{"area":{"name":"福岡","code":"82182"},"temps":["22","22","18","23"]},{"area":{"name":"八幡","code":"82056"},"temps":["21","21","18","23"]},{"area":{"name":"飯塚","code":"82136"},"temps":["21","21","17","24"]},{"area":{"name":"久留米","code":"82306"},"temps":["23","23","18","26"]}]}]},{"publishingOffice":"福岡管区気象台","reportDatetime":"2023-05-19T11:00:00+09:00","timeSeries":[{"timeDefines":["2023-05-20T00:00:00+09:00","2023-05-21T00:00:00+09:00","2023-05-22T00:00:00+09:00","2023-05-23T00:00:00+09:00","2023-05-24T00:00:00+09:00","2023-05-25T00:00:00+09:00","2023-05-26T00:00:00+09:00"],"areas":[{"area":{"name":"福岡県","code":"400000"},"weatherCodes":["211","101","200","200","101","101","101"],"pops":["","10","40","40","10","10","10"],"reliabilities":["","","B","C","A","A","A"]}]},{"timeDefines":["2023-05-20T00:00:00+09:00","2023-05-21T00:00:00+09:00","2023-05-22T00:00:00+09:00","2023-05-23T00:00:00+09:00","2023-05-24T00:00:00+09:00","2023-05-25T00:00:00+09:00","2023-05-26T00:00:00+09:00"],"areas":[{"area":{"name":"福岡","code":"82182"},"tempsMin":["","17","17","16","14","15","16"],"tempsMinUpper":["","19","19","18","16","16","17"],"tempsMinLower":["","14","15","14","12","12","13"],"tempsMax":["","26","24","23","26","28","28"],"tempsMaxUpper":["","28","25","24","27","29","30"],"tempsMaxLower":["","23","22","20","23","25","25"]}]}],"tempAverage":{"areas":[{"area":{"name":"福岡","code":"82182"},"min":"17.0","max":"25.2"}]},"precipAverage":{"areas":[{"area":{"name":"福岡","code":"82182"},"min":"6.3","max":"29.6"}]}}]'
#print(k)
deta = json.loads(s)
deta1 = json.loads(k)
deta2 = 10
print(deta1)
x = ["following"],["present"],["previous"]
for t in []:
 print(deta["nowonair_list"]["g1"][t]["start_time"])
 print(deta["nowonair_list"]["g1"][t]["title"])



@app.route("/")
def html():
    return render_template('a.html',deta=deta)             

@app.route("/w")
def html1():
    return render_template('b.html',deta1=deta1) 

@app.route("/1")
def html2():
   return render_template('c.html',deta2=deta2)
            
if __name__ == "__main__":
   app.run(port=5120)
