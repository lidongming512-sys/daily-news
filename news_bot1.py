#!/usr/bin/env python3
"""
测试脚本 - 带详细错误信息
"""

import os
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

print("=" * 50)
print("🔍 开始邮件发送测试")
print("=" * 50)

# 打印环境变量（不显示完整密码）
sender = os.getenv('EMAIL_USER', 'NOT_SET')
password = os.getenv('EMAIL_PASS', 'NOT_SET')
receiver = os.getenv('RECEIVER_EMAIL', 'NOT_SET')

print(f"发件人: {sender}")
print(f"密码长度: {len(password) if password != 'NOT_SET' else 'NOT_SET'}")
print(f"收件人: {receiver}")

try:
    # 测试SMTP连接
    print("\n🔗 正在连接SMTP服务器...")
    server = smtplib.SMTP_SSL('smtp.qq.com', 465, timeout=10)
    print("✅ SMTP连接成功")
    
    print("\n🔐 正在登录邮箱...")
    server.login(sender, password)
    print("✅ 邮箱登录成功")
    
    # 创建测试邮件
    msg = MIMEText("这是一封测试邮件", 'plain', 'utf-8')
    msg['Subject'] = "📧 测试邮件 " + datetime.now().strftime("%H:%M:%S")
    msg['From'] = sender
    msg['To'] = receiver
    
    print("\n📤 正在发送邮件...")
    server.send_message(msg)
    print("✅ 邮件发送成功！")
    
    server.quit()
    print("\n🎉 测试完成！请检查邮箱")
    
except Exception as e:
    print(f"\n❌ 错误类型: {type(e).__name__}")
    print(f"❌ 错误信息: {str(e)}")
    print(f"\n🔧 常见原因:")
    print("1. 邮箱授权码错误")
    print("2. 邮箱未开启SMTP")
    print("3. 网络问题")
    print("4. 收件人邮箱错误")

print("=" * 50)
