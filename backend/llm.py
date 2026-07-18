"""GLM-5.2 大模型调用封装（OpenAI 兼容接口）。"""

import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# 尝试从多个位置加载 .env（本地开发用）
for candidate in [
    Path(__file__).resolve().parents[2] / ".env",   # project_root/.env
    Path(__file__).resolve().parent / ".env",         # backend/.env
    Path(".env"),                                     # cwd/.env
]:
    if candidate.exists():
        load_dotenv(candidate)
        break

API_KEY = os.getenv("GLM_API_KEY")
BASE_URL = os.getenv("GLM_BASE_URL", "https://open.bigmodel.cn/api/paas/v4/")
MODEL = os.getenv("GLM_MODEL", "glm-5.2")

_client = None


def get_client() -> OpenAI:
    global _client
    if _client is None:
        _client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
    return _client


SYSTEM_PROMPT = (
    "你是一个西方科学史知识助手。根据提供的科学家档案与关系数据，"
    "用简洁清晰的中文回答用户关于科学家成就、生平、学科和相互关系的问题。"
    "如果数据中没有相关信息，请如实说明，并可结合常识简要补充。"
)


def chat(question: str, graph_context: str) -> str:
    """调用 GLM-5.2 进行对话，返回回答文本。"""
    client = get_client()
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "system", "content": f"科学家数据：\n{graph_context}"},
            {"role": "user", "content": question},
        ],
        temperature=0.4,
        max_tokens=1024,
    )
    return resp.choices[0].message.content


if __name__ == "__main__":
    from graph import get_graph_context
    print(chat("牛顿和爱因斯坦之间有什么传承关系？", get_graph_context()))
