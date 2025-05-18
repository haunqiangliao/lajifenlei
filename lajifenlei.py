import streamlit as st

# 全面垃圾分类数据库（2023最新版）
TRASH_CLASSIFICATION = {
    "可回收物": [
        "报纸", "书本", "纸箱", "包装纸盒", "广告单", "快递纸箱", "打印纸",
        "塑料瓶", "塑料玩具", "塑料桶", "塑料衣架", "塑料包装盒", "泡沫塑料",
        "玻璃瓶", "玻璃杯", "窗户玻璃", "镜子", "酒瓶",
        "金属罐", "金属餐具", "金属文具", "金属厨具", "金属工具", "钥匙",
        "旧衣服", "旧鞋子", "旧包包", "床单", "窗帘", "毛绒玩具",
        "牛奶盒", "饮料盒", "纸杯", "纸餐盒"
    ],
    "有害垃圾": [
        "电池", "充电电池", "纽扣电池", "蓄电池", "荧光灯管", "节能灯",
        "药品", "药瓶", "药片", "胶囊", "温度计", "血压计",
        "化妆品", "指甲油", "染发剂", "消毒剂", "杀虫剂", "老鼠药",
        "油漆桶", "油漆", "油漆刷", "溶剂", "胶水", "强力胶",
        "X光片", "CT片", "相片底片", "废胶片"
    ],
    "湿垃圾": [
        "剩菜剩饭", "菜叶", "果皮", "果核", "果壳", "瓜子壳",
        "茶叶渣", "咖啡渣", "中药渣", "宠物饲料", "鱼骨头", "虾壳",
        "蛋壳", "面包", "饼干", "蛋糕", "糖果", "坚果",
        "花卉", "绿植", "落叶", "树枝", "盆栽", "花盆土",
        "过期食品", "腐烂水果", "发霉食物", "剩饭", "剩面", "剩粥"
    ],
    "干垃圾": [
        "餐巾纸", "卫生纸", "湿纸巾", "尿不湿", "卫生巾", "纸尿裤",
        "塑料袋", "食品包装袋", "保鲜膜", "保鲜袋", "快递包装", "气泡膜",
        "一次性餐具", "一次性杯子", "一次性餐盒", "牙签", "吸管", "筷子",
        "烟蒂", "烟灰", "打火机", "创可贴", "棉签", "化妆棉",
        "笔", "橡皮", "胶带", "橡皮泥", "干燥剂", "防潮剂",
        "大骨头", "贝壳", "硬果壳", "毛发", "宠物粪便", "猫砂",
        "脏抹布", "旧毛巾", "破碗", "陶瓷", "雨伞", "打火机",
        "口罩", "手套", "袜子", "内衣", "旧袜子", "旧内衣"
    ]
}

# 页面设置
st.set_page_config(
    page_title="上海垃圾分类小助手",
    page_icon="🗑️",
    layout="centered"
)

# 主界面
st.title("🗑️ 上海垃圾分类小助手")
st.write("输入垃圾名称，查询所属分类（2023最新版）")

# 搜索功能
col1, col2 = st.columns([3, 1])
with col1:
    user_input = st.text_input("请输入垃圾名称", placeholder="例如：电池、塑料袋...")
with col2:
    st.write("")
    st.write("")
    search_btn = st.button("查询")

if search_btn or user_input:
    user_input = user_input.strip()
    if user_input:
        found = False
        for category, items in TRASH_CLASSIFICATION.items():
            if user_input in items:
                st.success(f"『{user_input}』属于：{category}")
                found = True
                break
        
        if not found:
            st.warning(f"未找到『{user_input}』的分类，请尝试其他名称")

# 分类示例展示
st.divider()
st.subheader("2023年最新垃圾分类指南")

tabs = st.tabs(["可回收物", "有害垃圾", "湿垃圾", "干垃圾"])
for i, (category, items) in enumerate(TRASH_CLASSIFICATION.items()):
    with tabs[i]:
        st.write(f"#### {category}（共{len(items)}种）")
        cols = st.columns(3)
        for j, item in enumerate(items):
            cols[j%3].write(f"- {item}")

# 页脚
st.divider()
st.caption("数据根据《上海市生活垃圾管理条例（2023修订版）》整理")
st.caption("提示：不确定分类时请选择干垃圾")

# 添加搜索建议
if user_input and not found:
    st.info("💡 类似物品建议：")
    similar_items = []
    for items in TRASH_CLASSIFICATION.values():
        for item in items:
            if user_input in item:
                similar_items.append(item)
    
    if similar_items:
        st.write(", ".join(similar_items[:5]))
    else:
        st.write("暂无类似物品")
