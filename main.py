from fastapi import FastAPI
import uvicorn
import os
from datetime import datetime

app = FastAPI(title="My First AI Agent")

# یک صفحه ساده برای اینکه ببینیم سرویس بالا آمده
@app.get("/")
def read_root():
    return {
        "message": "سلام! من اولین Agent هوش مصنوعی شما هستم!",
        "time": str(datetime.now())
    }

# مسیر سلامت برای Render (Health Check)
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# یک مسیر شبیه‌سازی Agent (اینجا بعداً می‌توانی کد Tickscope را اضافه کنی)
@app.get("/agent")
def agent(query: str = ""):
    # اینجا قرار است با مدل‌های زبانی یا Tickscope کار کنیم
    # فعلاً یک پاسخ نمونه برمی‌گردانیم
    return {
        "query": query,
        "response": f"درخواست شما '{query}' دریافت شد. (منتظر اضافه شدن Tickscope هستیم!)"
    }

if __name__ == "__main__":
    # پورتی که Render به ما می‌دهد را از محیط变量 می‌خوانیم
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)