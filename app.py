import os

# 必要そうなライブラリを取りあえずコピペ（後々増えたり減ったりするはず）
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

# 空の辞書
# REGISTANTS = {}

# 人気な言語をあらかじめ用意しておく
LANGUAGES = [
    "Python",
    "C",
    "C++",
    "C#",
    "Java",
    "JavaScript",
    "VB",
    "SQL",
    "PHP",
    "Assembly language",
    "Ruby",
    "Go",
    "Kotlin",
    "AWS",
    "Swift",
    "HTML",
    "CSS"
]

# 起動時、必ずHomeが表示されるように
@app.route("/")
def home():
    # ただHome画面を表示するだけ
    return render_template('home.html')

# ログイン処理
@app.route("/login", methods=["GET", "POST"])
def login():
    # それまで保存されていたセッションを消去
    # session.clear()

    # # POST通信だった（フォームが送信された）場合
    # if request.method == "POST":

    #     # フォームの情報を取得
    #     login_id = request.form.get("login_id")
    #     login_pass = request.form.get("login_pass")

        # データベースとフォームの情報を照合（ユーザー名・パスワード）
        # セッションにidを代入
        # page移動

    # /loginにアクセスしただけの場合
    # else:
    return render_template("login.html")

# 登録処理
@app.route("/register", methods=["GET", "POST"])
def register():

    # POST通信だった（フォームが送信された）場合
    # if request.method == "POST":

    #     # フォームの情報を取得
    #     register_id = request.form.get("register_id")
    #     register_pass = request.form.get("register_pass")

        # 名前被りチェック
        # パスワードをハッシュ化
        # データベースにformのデータを記録
        # セッションにidを代入
        # page移動

    # /registerにアクセスしただけの場合
    # else:
    return render_template("register.html")

# 記録処理
# 中井が担当
@app.route("/record", methods=["GET", "POST"])
# @login_required
def record():

    if request.method == "POST":

        # エラー言語（選ぶ）formじゃないかも?
        language = request.form.get("language")
        # エラー
        error = request.form.get("error")
        # 状況説明
        explanation = request.form.get("explanation")
        # 解決策
        solution = request.form.get("solution")

        # apology 作らないといけない,helpers.pyみたいなの
        if not language:
            return apology("missing language", 400)


        if not error:
            return apology("please enter an error", 400)

        if not explanation:
            return apology("Please explain the situation", 400)

        # 未解決の場合（ボタンが押されたらにした方がいい？）
        if not solution:
            flash("記録しました！頑張ったね！")
            return render_template("outstanding.html")
            
        # 解決できた場合
        
        flash("記録しました！解決できてすごい！")

        else:
            flash("記録しました！解決できてすごい！")

            return render_template("resolved.html")

    else:
        return render_template("record.html")

#イシモリ
# 未解決のエラーを表示
@app.route("/outstanding")
# @login_required
def display_outstanding():

    # 未解決エラーをデータベースから取り出し、格納
    # outstanding_errors = db.execute("SELECT ~")

    return render_template("outstanding.html", outstanding_errors=outstanding_errors)

#解決済みのエラーを表示
@app.route("/resolved")
# @login_required
def display_resolved():

    # 解決済みのエラーをデータベースから取り出し、格納
    # resolved_errors = db.execute("SELECT ~")

    return render_template("outstanding.html", resolved_errors=resolved_errors)

#####イシモリ
if __name__ == "__main__":
    app.run(debug=True)