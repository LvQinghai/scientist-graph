"""西方科学家数据库：档案信息与学科分类。"""

# 学科列表
FIELDS = [
    {"id": "physics",   "name": "物理学",   "icon": "⚛️", "color": "#6366f1"},
    {"id": "math",      "name": "数学",     "icon": "📐", "color": "#10b981"},
    {"id": "chemistry", "name": "化学",     "icon": "🧪", "color": "#f59e0b"},
    {"id": "biology",   "name": "生物学",   "icon": "🧬", "color": "#ec4899"},
    {"id": "astronomy", "name": "天文学",   "icon": "🔭", "color": "#3b82f6"},
    {"id": "cs",        "name": "计算机科学", "icon": "💻", "color": "#8b5cf6"},
]

# 科学家档案：id -> {name, name_en, country, field, birth, death, achievements, bio}
SCIENTISTS = {
    # ===== 物理学 =====
    "galileo": {
        "name": "伽利略·伽利雷", "name_en": "Galileo Galilei",
        "country": "意大利", "field": "physics", "birth": 1564, "death": 1642,
        "achievements": ["近代物理学之父", "望远镜天文观测", "自由落体定律", "惯性原理"],
        "bio": "意大利天文学家、物理学家，被誉为现代科学之父。他改进了望远镜并用于天文观测，支持哥白尼的日心说，奠定了近代实验物理学的基础。"
    },
    "newton": {
        "name": "艾萨克·牛顿", "name_en": "Isaac Newton",
        "country": "英国", "field": "physics", "birth": 1643, "death": 1727,
        "achievements": ["万有引力定律", "经典力学三大定律", "微积分", "光学光谱分析"],
        "bio": "英国物理学家、数学家，科学革命的集大成者。他建立了经典力学体系，发现万有引力定律，与莱布尼茨各自独立发明微积分，著有《自然哲学的数学原理》。"
    },
    "faraday": {
        "name": "迈克尔·法拉第", "name_en": "Michael Faraday",
        "country": "英国", "field": "physics", "birth": 1791, "death": 1867,
        "achievements": ["电磁感应定律", "电解定律", "电动机原理", "磁场概念"],
        "bio": "英国物理学家、化学家，自学成才的科学巨匠。发现了电磁感应现象，为现代电气工业奠定了基础，提出了电场和磁场的概念。"
    },
    "maxwell": {
        "name": "詹姆斯·麦克斯韦", "name_en": "James Clerk Maxwell",
        "country": "英国", "field": "physics", "birth": 1831, "death": 1879,
        "achievements": ["麦克斯韦方程组", "电磁理论统一", "光电磁本质", "统计力学"],
        "bio": "苏格兰物理学家，完成了电磁理论的统一，用四个方程将电、磁、光统一为同一现象。爱因斯坦评价他的工作是自牛顿以来物理学最深刻的变化。"
    },
    "einstein": {
        "name": "阿尔伯特·爱因斯坦", "name_en": "Albert Einstein",
        "country": "德国/美国", "field": "physics", "birth": 1879, "death": 1955,
        "achievements": ["狭义相对论", "广义相对论", "光电效应", "质能方程 E=mc²"],
        "bio": "德裔美籍理论物理学家，20世纪最伟大的科学家。提出相对论彻底改变了人类对时空的认知，因光电效应解释获1921年诺贝尔物理学奖。"
    },
    "planck": {
        "name": "马克斯·普朗克", "name_en": "Max Planck",
        "country": "德国", "field": "physics", "birth": 1858, "death": 1947,
        "achievements": ["量子假说", "普朗克常数", "黑体辐射", "量子力学奠基"],
        "bio": "德国物理学家，量子论的创始人。1900年提出能量量子化假说，开启了量子物理学的新纪元，获1918年诺贝尔物理学奖。"
    },
    "bohr": {
        "name": "尼尔斯·玻尔", "name_en": "Niels Bohr",
        "country": "丹麦", "field": "physics", "birth": 1885, "death": 1962,
        "achievements": ["玻尔原子模型", "互补原理", "哥本哈根诠释", "量子力学"],
        "bio": "丹麦物理学家，量子力学的核心人物。提出原子结构模型，创立哥本哈根学派，获1922年诺贝尔物理学奖，对量子力学的诠释影响深远。"
    },
    "heisenberg": {
        "name": "沃纳·海森堡", "name_en": "Werner Heisenberg",
        "country": "德国", "field": "physics", "birth": 1901, "death": 1976,
        "achievements": ["不确定性原理", "矩阵力学", "量子力学", "同位旋概念"],
        "bio": "德国物理学家，量子力学的创立者之一。1927年提出不确定性原理，获1932年诺贝尔物理学奖，是玻尔在哥本哈根的学生和合作者。"
    },
    "curie": {
        "name": "玛丽·居里", "name_en": "Marie Curie",
        "country": "波兰/法国", "field": "physics", "birth": 1867, "death": 1934,
        "achievements": ["放射性研究", "发现镭和钋", "首位双诺奖得主", "放射化学"],
        "bio": "波兰裔法籍物理学家、化学家。研究放射性现象，发现钋和镭两种元素，是首位获得诺贝尔奖的女性，也是唯一在两个不同学科领域获奖的科学家。"
    },
    "feynman": {
        "name": "理查德·费曼", "name_en": "Richard Feynman",
        "country": "美国", "field": "physics", "birth": 1918, "death": 1988,
        "achievements": ["量子电动力学", "费曼图", "路径积分", "超流性理论"],
        "bio": "美国理论物理学家，20世纪最具魅力的科学家之一。在量子电动力学方面做出开创性贡献，发明费曼图，获1965年诺贝尔物理学奖。"
    },

    # ===== 数学 =====
    "euclid": {
        "name": "欧几里得", "name_en": "Euclid",
        "country": "古希腊", "field": "math", "birth": -300, "death": -270,
        "achievements": ["《几何原本》", "欧氏几何", "公理化方法", "数论基础"],
        "bio": "古希腊数学家，被称为几何之父。其著作《几何原本》是数学史上最有影响的著作之一，建立了公理化几何体系，影响西方数学两千余年。"
    },
    "archimedes": {
        "name": "阿基米德", "name_en": "Archimedes",
        "country": "古希腊", "field": "math", "birth": -287, "death": -212,
        "achievements": ["浮力定律", "杠杆原理", "穷竭法", "圆周率近似"],
        "bio": "古希腊数学家、物理学家，古代最伟大的科学家之一。发现了浮力定律和杠杆原理，其穷竭法被视为微积分的先驱，被后世尊为力学之父。"
    },
    "gauss": {
        "name": "卡尔·高斯", "name_en": "Carl Friedrich Gauss",
        "country": "德国", "field": "math", "birth": 1777, "death": 1855,
        "achievements": ["数论《算术研究》", "正态分布", "微分几何", "最小二乘法"],
        "bio": "德国数学家，被誉为数学王子。在数论、代数、统计、微分几何等领域均有开创性贡献，是历史上最伟大的数学家之一。"
    },
    "euler": {
        "name": "莱昂哈德·欧拉", "name_en": "Leonhard Euler",
        "country": "瑞士", "field": "math", "birth": 1707, "death": 1783,
        "achievements": ["欧拉公式", "图论奠基", "复分析", "微积分系统化"],
        "bio": "瑞士数学家，历史上最多产的数学家之一。在微积分、图论、数论等领域贡献巨大，欧拉公式 e^(iπ)+1=0 被誉为最美的数学公式。"
    },
    "riemann": {
        "name": "伯恩哈德·黎曼", "name_en": "Bernhard Riemann",
        "country": "德国", "field": "math", "birth": 1826, "death": 1866,
        "achievements": ["黎曼几何", "黎曼猜想", "黎曼积分", "复分析"],
        "bio": "德国数学家，黎曼几何的创始人，高斯的学生。其工作为爱因斯坦的广义相对论提供了数学基础，黎曼猜想是数学界最重要的未解问题之一。"
    },
    "turing": {
        "name": "艾伦·图灵", "name_en": "Alan Turing",
        "country": "英国", "field": "cs", "birth": 1912, "death": 1954,
        "achievements": ["图灵机", "计算机科学基础", "破解恩尼格玛密码", "人工智能概念"],
        "bio": "英国数学家、计算机科学家，计算机科学之父。提出图灵机模型奠定了现代计算机理论基础，二战期间破解德国恩尼格玛密码，提出图灵测试。"
    },

    # ===== 化学 =====
    "lavoisier": {
        "name": "安托万·拉瓦锡", "name_en": "Antoine Lavoisier",
        "country": "法国", "field": "chemistry", "birth": 1743, "death": 1794,
        "achievements": ["现代化学之父", "氧化学说", "质量守恒定律", "化学命名法"],
        "bio": "法国化学家，被誉为现代化学之父。推翻燃素说，建立氧化学说，提出质量守恒定律，建立了系统的化学命名法。"
    },
    "dalton": {
        "name": "约翰·道尔顿", "name_en": "John Dalton",
        "country": "英国", "field": "chemistry", "birth": 1766, "death": 1844,
        "achievements": ["原子论", "分压定律", "色盲研究", "原子量"],
        "bio": "英国化学家、物理学家。提出科学的原子论，为现代化学奠定了理论基础，同时首次系统描述了色盲现象。"
    },
    "mendeleev": {
        "name": "德米特里·门捷列夫", "name_en": "Dmitri Mendeleev",
        "country": "俄国", "field": "chemistry", "birth": 1834, "death": 1907,
        "achievements": ["元素周期表", "周期律", "预测未发现元素", "化学系统化"],
        "bio": "俄国化学家，发现了化学元素的周期性规律并编制了元素周期表，成功预测了多种当时尚未发现的元素的性质。"
    },
    "pauling": {
        "name": "莱纳斯·鲍林", "name_en": "Linus Pauling",
        "country": "美国", "field": "chemistry", "birth": 1901, "death": 1994,
        "achievements": ["化学键理论", "量子化学", "蛋白质结构", "两次诺奖"],
        "bio": "美国化学家，量子化学的先驱。在化学键理论和生物大分子结构方面做出开创性贡献，是少数两次获得诺贝尔奖的人之一。"
    },

    # ===== 生物学 =====
    "darwin": {
        "name": "查尔斯·达尔文", "name_en": "Charles Darwin",
        "country": "英国", "field": "biology", "birth": 1809, "death": 1882,
        "achievements": ["进化论", "自然选择", "物种起源", "生物地理学"],
        "bio": "英国生物学家，进化论的奠基人。通过环球考察提出以自然选择为核心的生物进化理论，著有《物种起源》，彻底改变了人类对生命起源的认识。"
    },
    "mendel": {
        "name": "格雷戈尔·孟德尔", "name_en": "Gregor Mendel",
        "country": "奥地利", "field": "biology", "birth": 1822, "death": 1884,
        "achievements": ["遗传学定律", "豌豆杂交实验", "显性隐性遗传", "遗传因子"],
        "bio": "奥地利修道士、生物学家，现代遗传学之父。通过豌豆杂交实验发现了遗传规律，其工作在去世后才被重新发现并影响深远。"
    },
    "pasteur": {
        "name": "路易·巴斯德", "name_en": "Louis Pasteur",
        "country": "法国", "field": "biology", "birth": 1822, "death": 1895,
        "achievements": ["巴氏消毒法", "微生物学说", "疫苗研发", "发酵理论"],
        "bio": "法国微生物学家、化学家。证明了微生物致病理论，发明巴氏消毒法，研制了狂犬病疫苗，被誉为微生物学之父。"
    },
    "watson": {
        "name": "詹姆斯·沃森", "name_en": "James Watson",
        "country": "美国", "field": "biology", "birth": 1928, "death": None,
        "achievements": ["DNA双螺旋结构", "分子生物学", "基因组研究"],
        "bio": "美国分子生物学家。与克里克共同发现DNA双螺旋结构，开启了分子生物学时代，获1962年诺贝尔生理学或医学奖。"
    },
    "crick": {
        "name": "弗朗西斯·克里克", "name_en": "Francis Crick",
        "country": "英国", "field": "biology", "birth": 1916, "death": 2004,
        "achievements": ["DNA双螺旋结构", "中心法则", "分子生物学"],
        "bio": "英国生物学家、物理学家。与沃森共同发现DNA双螺旋结构，提出分子生物学的中心法则，获1962年诺贝尔奖。"
    },

    # ===== 天文学 =====
    "copernicus": {
        "name": "尼古拉·哥白尼", "name_en": "Nicolaus Copernicus",
        "country": "波兰", "field": "astronomy", "birth": 1473, "death": 1543,
        "achievements": ["日心说", "天体运行论", "天文学革命"],
        "bio": "波兰天文学家，文艺复兴时期的天文学巨匠。提出日心说，推翻了统治千年的地心说，引发了天文学和世界观的革命。"
    },
    "kepler": {
        "name": "约翰内斯·开普勒", "name_en": "Johannes Kepler",
        "country": "德国", "field": "astronomy", "birth": 1571, "death": 1630,
        "achievements": ["行星运动三定律", "光学", "望远镜改良"],
        "bio": "德国天文学家。发现了行星运动三大定律，为牛顿万有引力定律的发现奠定了基础，是近代天文学的奠基人之一。"
    },
    "hubble": {
        "name": "埃德温·哈勃", "name_en": "Edwin Hubble",
        "country": "美国", "field": "astronomy", "birth": 1889, "death": 1953,
        "achievements": ["宇宙膨胀", "哈勃定律", "星系分类", "河外星系"],
        "bio": "美国天文学家。证明了银河系外存在其他星系，发现宇宙正在膨胀，为现代宇宙学奠定了基础，哈勃太空望远镜以其命名。"
    },

    # ===== 计算机科学 =====
    "von_neumann": {
        "name": "约翰·冯·诺依曼", "name_en": "John von Neumann",
        "country": "匈牙利/美国", "field": "cs", "birth": 1903, "death": 1957,
        "achievements": ["冯·诺依曼架构", "博弈论", "量子力学数学基础", "计算机科学"],
        "bio": "匈牙利裔美籍数学家，20世纪最伟大的通才科学家之一。提出冯·诺依曼计算机架构，奠定了现代计算机的结构基础，同时在博弈论、量子力学等领域贡献卓越。"
    },
    "shannon": {
        "name": "克劳德·香农", "name_en": "Claude Shannon",
        "country": "美国", "field": "cs", "birth": 1916, "death": 2001,
        "achievements": ["信息论", "比特概念", "数字电路设计", "密码学"],
        "bio": "美国数学家、工程师，信息论之父。1948年发表《通信的数学理论》，奠定了数字通信和信息时代的理论基础。"
    },
}


def get_fields_with_counts():
    """返回学科列表及每个学科的科学家数量。"""
    result = []
    for f in FIELDS:
        count = sum(1 for s in SCIENTISTS.values() if s["field"] == f["id"])
        result.append({**f, "count": count})
    return result


def get_scientists_by_field(field_id: str):
    """按学科返回科学家简要列表。"""
    return [
        {"id": sid, **{k: v for k, v in s.items() if k != "bio"}}
        for sid, s in SCIENTISTS.items()
        if s["field"] == field_id
    ]


def get_scientist(sid: str):
    """获取科学家完整档案。"""
    return SCIENTISTS.get(sid)


def search_scientists(query: str):
    """按姓名搜索科学家。"""
    q = query.lower()
    return [
        {"id": sid, "name": s["name"], "name_en": s["name_en"], "field": s["field"]}
        for sid, s in SCIENTISTS.items()
        if q in s["name"].lower() or q in s["name_en"].lower()
    ]


if __name__ == "__main__":
    for f in get_fields_with_counts():
        print(f"{f['icon']} {f['name']}: {f['count']} 人")
