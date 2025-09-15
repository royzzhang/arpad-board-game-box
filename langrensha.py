import random

import streamlit as st

with st.sidebar:
    player_count = st.slider('玩家数', min_value=6, max_value=20, value=9, step=1)
    player_names = [''] * player_count
    for i in range(player_count):
        player_names[i] = st.text_input(f'玩家{i + 1}')

st.title('狼人杀发牌器')

st.write(f'当前玩家数：{player_count}')

game_setup = st.form('game_setup')

game_setup.header('游戏配置')
anonymous_mode = game_setup.checkbox('匿名模式')

villager_count = game_setup.slider('村民数量', min_value=0, max_value=player_count, value=int(player_count / 3))
wolf_count = game_setup.slider('狼人数量（包括特殊狼）', min_value=0, max_value=player_count, value=int(player_count / 3))
gods = game_setup.multiselect('选择神职', options=['预言家', '女巫', '猎人', '守卫', '骑士', '长老', '白痴', '驯熊师'],
                              default=['预言家', '女巫', '猎人'], accept_new_options=True)
special_wolves = game_setup.multiselect('选择狼人方特殊角色', options=['黑狼王', '预言狼', '隐狼', '白狼王'],
                                        default=['黑狼王'], accept_new_options=True)
wolf_characters = ['狼人'] + [wolf for wolf in special_wolves if wolf != '隐狼']
neutrals = game_setup.multiselect('选择第三方角色', options=['吹笛人', '石像鬼', '丘比特', '白狼'], accept_new_options=True)
characters = ['村民'] * villager_count + ['狼人'] * (wolf_count - len(special_wolves)) + gods + special_wolves + neutrals

setup_complete = game_setup.form_submit_button('发牌')
if setup_complete:
    random.shuffle(characters)

    st.header('分配结果')
    if len(characters) != player_count:
        st.write(f'玩家数({player_count})与角色数({len(characters)})不匹配！')
    elif len(special_wolves) > wolf_count:
        st.write('特殊狼数量多于总狼人数！')
    else:
        st.write('请点击下方文本框右上角直接复制分配结果。')
        if anonymous_mode:
            random.shuffle(player_names)
        output_string = ''
        for i in range(player_count):
            output_string += f'{i + 1}({player_names[i]}){characters[i]}\n'
        if anonymous_mode:
            output_string += f'狼人是{[i + 1 for i, x in enumerate(characters) if x in wolf_characters]}\n'
        output_string += f'首夜随机刀目标是{random.choice([i + 1 for i, x in enumerate(characters) if x not in wolf_characters])}。'
        st.code(output_string, language=None)
