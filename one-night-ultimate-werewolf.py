import random

import streamlit as st

with st.sidebar:
    player_count = st.slider('玩家数', min_value=3, max_value=10, value=6, step=1)
    player_names = [''] * player_count
    for i in range(player_count):
        player_names[i] = st.text_input(f'玩家{i + 1}')

st.title('一夜终极狼人发牌器')

st.write(f'当前玩家数：{player_count}')
st.write(f'应有角色数：{player_count + 3} (若加入始祖狼则+1)')

game_setup = st.form('game_setup')

game_setup.header('游戏配置')
anonymous_mode = game_setup.checkbox('匿名模式')

center_wolf = []
villager_count = game_setup.slider('村民数量', min_value=0, max_value=3, value=1)
wolf_count = game_setup.slider('普通狼人数量', min_value=0, max_value=2, value=2)
gods = game_setup.multiselect('选择神职',
                              options=['守夜人', '预言家', '强盗', '捣蛋鬼', '酒鬼', '失眠者', '猎人', '化身幽灵', '皮匠', '哨兵', '见习预言家', '白痴', '告密者', '监护人', '保镖', '灵异侦探', '女巫'],
                              default=['预言家', '强盗', '捣蛋鬼'], accept_new_options=True)
special_wolves = game_setup.multiselect('选择狼人方特殊角色', options=['爪牙', '始祖狼', '狼先知', '贪睡狼'],
                                        default=[], accept_new_options=True)
wolf_characters = ['狼人'] * wolf_count + [wolf for wolf in special_wolves if wolf != '爪牙']

non_wolves = ['村民'] * villager_count + gods
if '守夜人' in gods:
    non_wolves += ['守夜人']
wolves = ['狼人'] * wolf_count + special_wolves
if '始祖狼' in wolves:
    random.shuffle(wolves)
    center_wolf = [wolves.pop()]
characters = non_wolves + wolves

token = random.choice(['变狼人', '变村民', '变皮匠', '沉默', '无事发生'])
setup_complete = game_setup.form_submit_button('发牌')
if setup_complete:
    random.shuffle(characters)

    st.header('分配结果')
    if len(characters + center_wolf) != (player_count + 3 if '始祖狼' not in wolf_characters else player_count + 4):
        st.write(f'当前角色数({len(characters + center_wolf)})与应有角色数({player_count + 3 if '始祖狼' not in wolf_characters else player_count + 4})不匹配！')
    else:
        st.write('请点击下方文本框右上角直接复制分配结果。')
        if anonymous_mode:
            random.shuffle(player_names)
        output_string = ''
        for i in range(player_count):
            output_string += f'{i + 1}({player_names[i]}){characters[i]}\n'
        for i in range(3):
            output_string += f'无主牌{1 + i}{characters[player_count + i]}\n'
        if '始祖狼' in wolf_characters:
            output_string += f'无主狼牌 {center_wolf[0]}\n'
        if '监护人' in gods:
            output_string += f'指示物 {token}\n'
        st.code(output_string, language=None)
