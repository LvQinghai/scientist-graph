#!/bin/bash
# 西方科学家图谱 - 一键启动脚本
# 使用方法: bash start.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR/backend"

# 检查 .env 是否存在
if [ ! -f "$SCRIPT_DIR/../.env" ] && [ ! -f "$SCRIPT_DIR/.env" ]; then
    echo "============================================"
    echo "  首次运行需要配置 API Key"
    echo "============================================"
    echo ""
    echo "请将 .env.example 复制为 .env 并填入你的 API Key:"
    echo "  cp .env.example .env"
    echo "  然后编辑 .env 文件，填入 GLM_API_KEY"
    echo ""
    exit 1
fi

# 检查依赖是否安装
echo ">>> 检查 Python 依赖..."
python3 -c "import fastapi, uvicorn, networkx, openai, dotenv" 2>/dev/null || {
    echo ">>> 依赖未安装，正在安装..."
    pip install -r ../requirements.txt
}

echo ""
echo "============================================"
echo "  西方科学家图谱 启动中..."
echo "  访问地址: http://localhost:8001"
echo "  按 Ctrl+C 停止服务"
echo "============================================"
echo ""

python3 main.py
