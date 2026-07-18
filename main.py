"""Railway 部署入口。"""

import os
import sys

# 将 backend/ 加入模块搜索路径，让其中模块可被直接导入
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "backend"))

# 从 backend/app.py 导入 app 并暴露为模块级属性，供 uvicorn 加载
from app import app  # noqa: E402

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
