import streamlit as st

st.title('阿尔帕德桌游盒')
st.write('请点击上方选择切换界面。')
st.write('请点击左上方箭头打开工具栏以更改玩家人数或修改玩家昵称。再次点击箭头可关闭工具栏。')

st.header('狼人杀')
if st.checkbox('显示狼人杀规则'):
    with open('rules_markdown/langrensha_rules.md', 'r', encoding='utf-8') as f:
        st.markdown(f.read())

st.header('阿瓦隆')
if st.checkbox('显示阿瓦隆规则'):
    with open('rules_markdown/avalon_rules.md', 'r', encoding='utf-8') as f:
        st.markdown(f.read())

st.header('亚瑟传奇')
if st.checkbox('显示亚瑟传奇规则'):
    with open('rules_markdown/quest_rules.md', 'r', encoding='utf-8') as f:
        st.markdown(f.read())

st.header('斗地主')
if st.checkbox('显示斗地主规则'):
    st.write('不会吧不会吧，不会5202年都还有人不会玩斗地主吧？')