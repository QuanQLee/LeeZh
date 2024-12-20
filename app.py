from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 用于会话和消息闪pip install flask flask-mail -i https://pypi.tuna.tsinghua.edu.cn/simple


# 配置邮件（用于联系表单）
app.config['MAIL_SERVER'] = 'smtp.example.com'  # 替换为你的SMTP服务器
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@example.com'  # 替换为你的邮箱
app.config['MAIL_PASSWORD'] = 'your_email_password'  # 替换为你的邮箱密码

mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # 发送邮件
        msg = Message('新联系表单提交',
                      sender=app.config['MAIL_USERNAME'],
                      recipients=['your_email@example.com'])  # 接收联系表单的邮箱
        msg.body = f"来自 {name} ({email}) 的消息:\n\n{message}"

        try:
            mail.send(msg)
            flash('消息已成功发送！', 'success')
            return redirect(url_for('contact'))
        except Exception as e:
            print(e)
            flash('发送失败，请稍后再试。', 'danger')
            return redirect(url_for('contact'))

    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
