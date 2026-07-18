"""科学家关系图谱：师生、传承、合作等关系。"""

import networkx as nx
from scientists import SCIENTISTS

# 关系：(源, 目标, 类型, 说明)
# 类型：mentor(师生) / influence(传承影响) / collaboration(合作)
RELATIONS = [
    # 古代传承
    ("euclid", "archimedes", "influence", "几何学传承"),
    # 天文学传承链
    ("copernicus", "kepler", "influence", "日心说的继承与发展"),
    ("copernicus", "galileo", "influence", "日心说的观测验证"),
    ("kepler", "newton", "influence", "行星运动定律启发万有引力"),
    ("galileo", "newton", "influence", "实验物理到经典力学的传承"),
    # 牛顿的师承
    # 物理学传承链
    ("faraday", "maxwell", "influence", "电磁感应到电磁理论统一"),
    ("maxwell", "einstein", "influence", "电磁理论启发相对论"),
    # 量子力学传承
    ("planck", "einstein", "influence", "量子假说启发光电效应解释"),
    ("planck", "bohr", "influence", "量子理论到原子模型"),
    ("bohr", "heisenberg", "mentor", "哥本哈根学派师生"),
    ("einstein", "feynman", "influence", "相对论到量子电动力学的思想影响"),
    # 化学传承
    ("lavoisier", "dalton", "influence", "氧化学说到原子论"),
    ("dalton", "mendeleev", "influence", "原子论到元素周期表"),
    # 生物学
    ("mendel", "watson", "influence", "遗传学定律到分子遗传学"),
    ("watson", "crick", "collaboration", "共同发现DNA双螺旋结构"),
    # 数学
    ("gauss", "riemann", "mentor", "哥廷根大学师生"),
    ("euler", "gauss", "influence", "分析方法的影响"),
    # 计算机科学
    ("turing", "von_neumann", "influence", "计算理论到计算机架构"),
    ("shannon", "von_neumann", "collaboration", "信息论与计算架构的交流"),
    # 跨学科
    ("newton", "euler", "influence", "微积分的发展与推广"),
    ("curie", "pauling", "influence", "放射化学到量子化学"),
]


def build_graph() -> nx.DiGraph:
    g = nx.DiGraph()
    for sid, info in SCIENTISTS.items():
        g.add_node(sid, name=info["name"], field=info["field"])
    for src, dst, rel, desc in RELATIONS:
        g.add_edge(src, dst, relation=rel, desc=desc)
    return g


GRAPH = build_graph()

RELATION_LABELS = {
    "mentor": "师生",
    "influence": "传承",
    "collaboration": "合作",
}

RELATION_COLORS = {
    "mentor": "#ef4444",
    "influence": "#3b82f6",
    "collaboration": "#10b981",
}


def get_graph_data():
    """返回前端可视化用的 nodes / edges。"""
    field_colors = {
        "physics": "#6366f1", "math": "#10b981", "chemistry": "#f59e0b",
        "biology": "#ec4899", "astronomy": "#3b82f6", "cs": "#8b5cf6",
    }
    nodes = []
    for sid, info in SCIENTISTS.items():
        nodes.append({
            "id": sid,
            "label": info["name"],
            "field": info["field"],
            "color": field_colors.get(info["field"], "#64748b"),
        })
    edges = []
    for idx, (src, dst, rel, desc) in enumerate(RELATIONS):
        edges.append({
            "id": idx, "from": src, "to": dst,
            "label": RELATION_LABELS.get(rel, rel),
            "type": rel, "desc": desc,
            "color": RELATION_COLORS.get(rel, "#cbd5e1"),
        })
    return {"nodes": nodes, "edges": edges}


def get_relations_of(sid: str):
    """获取某科学家的所有关系（出边+入边）。"""
    result = []
    for src, dst, rel, desc in RELATIONS:
        label = RELATION_LABELS.get(rel, rel)
        if src == sid:
            result.append({"type": rel, "label": label, "desc": desc,
                           "target": dst, "target_name": SCIENTISTS[dst]["name"],
                           "direction": "→"})
        elif dst == sid:
            result.append({"type": rel, "label": label, "desc": desc,
                           "source": src, "source_name": SCIENTISTS[src]["name"],
                           "direction": "←"})
    return result


def get_graph_context() -> str:
    """生成知识图谱的文本描述，供 AI 回答使用。"""
    lines = ["以下是西方科学史上重要科学家及其关系数据：", "", "【科学家名单】"]
    for sid, s in SCIENTISTS.items():
        era = f"{s['birth']}~{s['death']}" if s['death'] else f"{s['birth']}~至今"
        lines.append(f"- {s['name']}（{s['name_en']}），{s['country']}，{era}，"
                     f"学科：{s['field']}。主要成就：{'、'.join(s['achievements'])}")
    lines.append("")
    lines.append("【科学家之间的关系】")
    for src, dst, rel, desc in RELATIONS:
        label = RELATION_LABELS.get(rel, rel)
        lines.append(f"- {SCIENTISTS[src]['name']} → {SCIENTISTS[dst]['name']}："
                     f"{label}关系（{desc}）")
    return "\n".join(lines)


def _match_scientists(text: str) -> list[str]:
    """从文本中提取匹配的科学家 ID。
    支持：全名、简写名、英文名、成就关键词匹配。
    """
    related = []
    t = text.lower()
    for sid, s in SCIENTISTS.items():
        name = s["name"]
        name_en = s["name_en"].lower()
        matched = False
        # 全名匹配
        if name in text or name_en in t:
            matched = True
        # 简写匹配：如"牛顿"匹配"艾萨克·牛顿"
        if not matched:
            short_name = name.split("·")[-1] if "·" in name else name
            if short_name in text or short_name.lower() in t:
                matched = True
        # 英文姓氏匹配
        if not matched:
            surname = name_en.split()[-1] if name_en else ""
            if surname and len(surname) >= 3 and surname in t:
                matched = True
        # 成就关键词匹配：如"DNA双螺旋"匹配沃森/克里克
        if not matched:
            for ach in s["achievements"]:
                # 取成就中较长的关键词（>=4字）进行模糊匹配
                for keyword in set(ach.replace("·", "").replace(" ", "").split("、")):
                    kw = keyword if isinstance(keyword, str) else ach.replace("·", "").replace(" ", "")
                    if len(kw) >= 4 and kw in text:
                        matched = True
                        break
                    # 尝试取成就的前6个字
                    short_kw = ach.replace("·", "").replace(" ", "")[:6]
                    if len(short_kw) >= 4 and short_kw in t:
                        matched = True
                        break
        if matched:
            related.append(sid)
    return related


def get_related_nodes(query: str) -> list[str]:
    """从文本中提取相关科学家 id，并扩展至关联节点，用于前端高亮。"""
    related = _match_scientists(query)
    highlight = set(related)
    for sid in related:
        highlight.update(GRAPH.successors(sid))
        highlight.update(GRAPH.predecessors(sid))
    return list(highlight)


if __name__ == "__main__":
    print(get_graph_context())
