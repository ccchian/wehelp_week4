#載入flask模組
from flask import Flask,request,render_template,redirect,session,url_for

app = Flask(__name__)

#設定 session 密鑰
app.secret_key='keysecrect'

@app.route('/')
def index():
    return render_template("signin.html")

#session ['參數名稱‘] = ‘資料’
# 跳轉到成功頁面：1.輸入帳密2.有登入狀態
#redirect 導向另一個路徑/也可直接傳送網址，導到路徑
@app.route('/signin',methods=['POST'])
def signin(): 
    account = request.form['account']  
    pwd = request.form["password"]
    if (account == "test" and pwd == "test") or session['login'] == 'alreadylogin':
        session['login'] = 'alreadylogin'
        return redirect(url_for("member")) 
    elif account == '' and pwd == '' :
        return redirect('http://127.0.0.1:3000/error?message=請輸入帳號密碼') 
    else:
        return redirect(url_for("error")) 

# 需經過render_template才能將路徑渲染到畫面上，導到前端

@app.route('/member')
def member():
    if session['login'] == 'alreadylogin':
       return render_template("member.html") 
    else :
       return redirect("/")
    
#設定wrongmess參數去取得要求物件，
@app.route('/error')
def error():
    wrongmess=request.args.get('message','帳號、或密碼輸入錯誤')
    return render_template("error.html",wrongmess2=wrongmess)


@app.route('/signout',)
def signout():
    session['login'] = 'none'
    return redirect('/')
     
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000)