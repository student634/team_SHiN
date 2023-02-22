import os

# 必要そうなライブラリを取りあえずコピペ（後々増えたり減ったりするはず）
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

# 起動時、必ずHomeが表示されるように
@app.route("/")
def home():
    # ただHome画面を表示するだけ
    # return render.template('home.html')#############
    return render_template('home.html')

# ログイン処理
@app.route("/login", methods=["GET", "POST"])
def login():
    # それまで保存されていたセッションを消去
    session.clear()

    # POST通信だった（フォームが送信された）場合
    if request.method == "POST":

        # フォームの情報を取得
        login_id = request.form.get("login_id")
        login_pass = request.form.get("login_pass")

        # データベースとフォームの情報を照合（ユーザー名・パスワード）
        # セッションにidを代入
        # page移動

    # /loginにアクセスしただけの場合
    else:
        return render_template("login.html")

<<<<<<< HEAD
# 登録処理
@app.route("/register", methods=["GET", "POST"])
def register():

    # POST通信だった（フォームが送信された）場合
    if request.method == "POST":

        # フォームの情報を取得
        register_id = request.form.get("register_id")
        register_pass = request.form.get("register_pass")

        # 名前被りチェック
        # パスワードをハッシュ化
        # データベースにformのデータを記録
        # セッションにidを代入
        # page移動

    # /registerにアクセスしただけの場合
    else:
        return render_template("register.html")
=======
# 未解決のエラーを表示
@app.route("/outstanding")
# @login_required
def display_outstanding():

    # 未解決エラーをデータベースから取り出し、格納
    outstanding_errors = db.execute("SELECT ~")

    return render_template("outstanding.html", outstanding_errors=outstanding_errors)

#解決済みのエラーを表示
@app.route("/resolved")
# @login_required
def display_resolved():

    # 未解決エラーをデータベースから取り出し、格納
    resolved_errors = db.execute("SELECT ~")

    return render_template("outstanding.html", resolved_errors=resolved_errors)

>>>>>>> refs/remotes/origin/main
