import streamlit as st

st.title('阿尔帕德桌游盒')
st.write('''
请点击上方选择切换界面。

请点击左上方箭头打开工具栏以更改玩家人数或修改玩家昵称。再次点击箭头可关闭工具栏。

以下规则默认使用本桌游盒附带发牌器且游玩方式为线上文字。
''')

st.header('狼人杀')
if st.toggle('显示狼人杀规则'):
    with open('rules_markdown/langrensha_rules.md', 'r', encoding='utf-8') as f:
        st.markdown(f.read())

st.header('阿瓦隆')
if st.toggle('显示阿瓦隆规则'):
    with open('rules_markdown/avalon_rules.md', 'r', encoding='utf-8') as f:
        st.markdown(f.read())

st.header('亚瑟传奇')
if st.toggle('显示亚瑟传奇规则'):
    with open('rules_markdown/quest_rules.md', 'r', encoding='utf-8') as f:
        st.markdown(f.read())

st.header('斗地主')
if st.toggle('显示斗地主规则'):
    st.write('不会吧不会吧，不会5202年都还有人不会玩斗地主吧？')

st.header('一夜终极狼人')
if st.toggle('显示一夜终极狼人规则'):
    with open('rules_markdown/one_night_ultimate_werewolf_rules.md', 'r', encoding='utf-8') as f:
        st.markdown(f.read())
