#!/usr/bin/env python3
"""
最简单的新闻简讯机器人
小白专用版
"""

import os
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import random

class SimpleNewsSender:
    def __init__(self):
        # 这些信息会在GitHub后台设置，这里不用改
        self.sender = os.getenv('EMAIL_USER')
        self.password = os.getenv('EMAIL_PASS') 
        self.receiver = os.getenv('RECEIVER_EMAIL')
    
    def get_daily_news(self):
        """生成今日新闻简讯"""
        today = datetime.now().strftime("%m月%d日")
        
        # 新闻分类
        news_categories = [
            "国内：经济社会发展稳步推进，各地重点项目建设加快",
            "国际：多边合作持续深化，国际交流更加密切", 
            "科技：创新驱动发展，数字技术应用拓展",
            "财经：市场运行平稳，消费活力持续恢复",
            "民生：基本保障完善，公共服务优化提升",
            "文化：精神生活丰富，文化活动多样",
            "健康：医疗服务改善，健康意识增强",
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
        
        # 组合内容
        content = f"📰 【每日新闻简讯】{today}\n\n"
        content += "="*40 + "\n\n"
        
        # 添加新闻
        for i, news in enumerate(news_categories[:6], 1):
            content += f"{i}. {news}\n\n"
        
        content += "="*40 + "\n\n"
        content += "✨ 每日一句\n"
        content += random.choice(quotes) + "\n\n"
        content += "="*40 + "\n"
        content += "📧 自动发送，无需回复\n"
        content += f"⏰ {datetime.now().strftime('%H:%M:%S')}\n"
        content += "💝 祝您生活愉快！"
        
        return content
    
    def send_email(self):
        """发送邮件"""
        try:
            print("🤖 开始发送每日新闻...")
            
            # 获取内容
            content = self.get_daily_news()
            today = datetime.now().strftime("%Y年%m月%d日")
            
            # 创建邮件
            msg = MIMEText(content, 'plain', 'utf-8')
            msg['Subject'] = f"📰 每日新闻简讯 {today}"
            msg['From'] = self.sender
            msg['To'] = self.receiver
            
            # 发送邮件（QQ邮箱）
            with smtplib.SMTP_SSL('smtp.qq.com', 465) as server:
                server.login(self.sender, self.password)
                server.send_message(msg)
            
            print(f"✅ 发送成功！时间：{datetime.now().strftime('%H:%M:%S')}")
            return True
            
        except Exception as e:
            print(f"❌ 发送失败：{str(e)}")
            return False

# 主程序
if __name__ == "__main__":
    print("="*50)
    print("📰 每日新闻简讯机器人")
    print("="*50)
    
    sender = SimpleNewsSender()
    success = sender.send_email()
    
    if success:
        print("🎉 任务完成！请检查您的邮箱")
    else:
        print("😅 发送失败，请检查配置")
    print("="*50)
