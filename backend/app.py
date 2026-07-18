"""FastAPI 主程序：学科浏览、科学家详情、关系图谱、AI 问答。"""

from pathlib import Path

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from scientists import (
    get_fields_with_counts, get_scientists_by_field, get_scientist, search_scientists,
)
from graph import get_graph_data, get_relations_of, get_graph_context, get_related_nodes
from llm import chat

app = FastAPI(title="西方科学家图谱")

# CORS：允许 Netlify 前端跨域访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 发布后可替换为具体的 Netlify 域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

STATIC_DIR = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


class ChatRequest(BaseModel):
    question: str


@app.get("/")
async def index():
    return HTMLResponse((STATIC_DIR / "index.html").read_text(encoding="utf-8"))


@app.get("/api/fields")
async def api_fields():
    """学科列表及科学家数量。"""
    return get_fields_with_counts()


@app.get("/api/scientists")
async def api_scientists(field: str = Query(...)):
    """按学科返回科学家列表。"""
    return get_scientists_by_field(field)


@app.get("/api/scientist/{sid}")
async def api_scientist_detail(sid: str):
    """科学家完整档案 + 相关关系。"""
    s = get_scientist(sid)
    if not s:
        return {"error": "not found"}
    relations = get_relations_of(sid)
    return {**s, "id": sid, "relations": relations}


@app.get("/api/search")
async def api_search(q: str = Query(...)):
    """按姓名搜索科学家。"""
    return search_scientists(q)


@app.get("/api/graph")
async def api_graph():
    """完整关系图谱数据。"""
    return get_graph_data()


@app.post("/api/chat")
def api_chat(req: ChatRequest):
    """AI 对话：基于科学家图谱回答问题，返回需高亮的节点。"""
    context = get_graph_context()
    answer = chat(req.question, context)
    # 综合问题和回答文本进行姓名匹配，确保高亮覆盖面更广
    highlight = get_related_nodes(req.question + " " + answer)
    return {"answer": answer, "highlight": highlight}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8001, reload=True)
