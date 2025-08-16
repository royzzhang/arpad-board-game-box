import streamlit as st

pages = {
    '桌游列表': [
        st.Page('langrensha.py', title='狼人杀'),
        st.Page('avalon.py', title='阿瓦隆'),
        st.Page('quest.py', title='亚瑟传奇'),
        st.Page('doudizhu.py', title='斗地主')
    ]
}

st.navigation([st.Page('arpad_board_game_box.py', title='主页'), pages]).run()