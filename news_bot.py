#!/usr/bin/env python3
"""
修正版新闻简讯机器人
修复了字符串编码问题
"""

import os
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import random

class SimpleNewsSender:
    def __init__(self):
        # 从环境变量获取配置
        self.sender = os.getenv('EMAIL_USER', '').strip()
        self.password = os.getenv('EMAIL_PASS', '').strip()
        self.receiver = os.getenv('RECEIVER_EMAIL', '').strip()
        
        print(f"📧 配置检查:")
        print(f"  发件人: {'已设置' if self.sender else '未设置'}")
        print(f"  密码: {'已设置' if self.password else '未设置'}")
        print(f"  收件人: {'已设置' if self.receiver else '未设置'}")
    
    def get_daily_news(self):
        """生成今日新闻简讯"""
        today = datetime.now().strftime("%m月%d日")
        
        # 新闻分类
        news_items = [
            "国内：经济社会发展稳步推进，各地重点项目建设加快",
            "国际：多边合作持续深化，国际交流更加密切", 
            "科技：创新驱动发展，数字技术应用拓展",
            "财经：市场运行平稳，消费活力持续恢复",
            "民生：基本保障完善，公共服务优化提升",
            "提醒：关注天气变化，注意出行安全"
        ]
        
        # 每日一句
        quotes = [
            "📚 知识改变命运，学习成就未来",
            "🌞 保持积极心态，拥抱美好生活", 
            "💪 坚持就是胜利，努力必有收获",
            "❤️ 关爱他人，温暖自己",
            "🚀 勇于创新，敢于追梦"
        ]
        
        # 组合内容 - 确保所有部分都是字符串
        content = f"📰 【每日新闻简讯】{today}\n\n"
        content += "=" * 40 + "\n\n"
        
        for i, news in enumerate(news_items, 1):
            content += f"{i}. {news}\n\n"
        
        content += "=" * 40 + "\n\n"
        content += "✨ 每日一句\n"
        content += random.choice(quotes) + "\n\n"
        content += "=" * 40 + "\n"
        content += "📧 自动发送，无需回复\n"
        content += f"⏰ 发送时间: {datetime.now().strftime('%H:%M:%S')}\n"
        content += "💝 祝您生活愉快！"
        
        return content
    
    def send_email(self):
        """发送邮件"""
        try:
            print("🤖 开始发送每日新闻...")
            
            # 检查配置
            if not all([self.sender, self.password, self.receiver]):
                print("❌ 配置不完整，请检查GitHub Secrets设置")
                return False
            
            # 获取内容
            content = self.get_daily_news()
            today = datetime.now().strftime("%Y年%m月%d日")
            
            # 创建邮件
            msg = MIMEText(content, 'plain', 'utf-8')
            msg['Subject'] = f"📰 每日新闻简讯 {today}"
            msg['From'] = self.sender
            msg['To'] = self.receiver
            
            print(f"📨 准备发送到: {self.receiver}")
            
            # 发送邮件
            print("🔗 连接到 smtp.qq.com:465...")
            with smtplib.SMTP_SSL('smtp.qq.com', 465, timeout=10) as server:
                print("✅ 连接成功")
                print("🔐 正在登录...")
                server.login(self.sender, self.password)
                print("✅ 登录成功")
                print("📤 发送邮件...")
                server.send_message(msg)
                print("✅ 邮件已发送")
            
            print(f"🎉 发送成功！时间：{datetime.now().strftime('%H:%M:%S')}")
            return True
            
        except smtplib.SMTPAuthenticationError as e:
            error_msg = str(e)
            print(f"❌ 认证失败：{error_msg}")
            print("💡 可能的原因：")
            print("   1. 邮箱密码/授权码错误")
            print("   2. 邮箱未开启SMTP服务")
            print("   3. QQ邮箱需要授权码，不是登录密码")
            return False
        except smtplib.SMTPException as e:
            error_msg = str(e)
            print(f"❌ SMTP错误：{error_msg}")
            return False
        except Exception as e:
            # 确保错误信息是字符串
            if isinstance(e, bytes):
                error_msg = e.decode('utf-8', errors='ignore')
            else:
                error_msg = str(e)
            print(f"❌ 发送失败：{error_msg}")
            return False

# 主程序
if __name__ == "__main__":
    print("=" * 50)
    print("📰 每日新闻简讯机器人")
    print("=" * 50)
    
    sender = SimpleNewsSender()
    success = sender.send_email()
    
    if success:
        print("🎉 任务完成！请检查您的邮箱")
    else:
        print("😅 发送失败，请查看上方错误信息")
    print("=" * 50)
