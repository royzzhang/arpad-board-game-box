import random

import streamlit as st

with st.sidebar:
    player_count = st.slider('玩家数', min_value=4, max_value=10, value=5, step=1)
    player_names = [''] * player_count
    for i in range(player_count):
        player_names[i] = st.text_input(f'玩家{i + 1}')

st.title('亚瑟传奇发牌器')
st.write(f'当前玩家数：{player_count}')

director_cut = st.checkbox('导演剪辑版')
youth_or_trickster = '青年'
if director_cut and player_count >= 6:
    youth_or_trickster = st.pills('选择加入青年或捣蛋鬼：', ['青年', '捣蛋鬼'], default='青年')

characters = ['摩根勒菲', '盲猎人']
if not director_cut:
    if player_count < 6:
        while len(characters) < player_count:
            characters.append('忠臣')
    else:
        characters += ['牧师', '公爵', '青年', '爪牙']
        if player_count >= 7:
            characters.append('捣蛋鬼')
            if player_count >= 8:
                characters.append('忠臣')
                if player_count >= 9:
                    characters.append('大公')
                    if player_count == 10:
                        characters.append('爪牙')
else:
    if player_count < 6:
        characters += random.sample(['牧师', '青年', '忠臣'], 2)
        if player_count == 5:
            characters.append('爪牙')
    elif 6 <= player_count < 9:
        characters += [youth_or_trickster, '牧师', '公爵', '爪牙']
        if player_count >= 7:
            characters.append('爪牙')
            if player_count == 8:
                characters.append('忠臣')
    else:
        characters += [youth_or_trickster, '牧师', '大公', '忠臣'] + ['爪牙'] * 3
        if player_count == 10:
            characters.append('公爵')
random.shuffle(characters)

starting_leader = random.choice(range(player_count)) + 1
reds = [characters.index('摩根勒菲') + 1]
cleric_sees = [characters.index('摩根勒菲') + 1, characters.index('盲猎人') + 1]
if '爪牙' in characters:
    minion_numbers = [i + 1 for i, x in enumerate(characters) if x == '爪牙']
    cleric_sees += minion_numbers
    reds += minion_numbers
if '捣蛋鬼' in characters:
    cleric_sees.append(characters.index('捣蛋鬼') + 1)

output_string = ''
red_statement = '，和{}之间彼此知道是红方' + f'以及{characters.index('盲猎人') + 1}是盲猎人。\n'
if director_cut and player_count >= 6:
    red_statement = '，和{}之间彼此知道是红方。\n'
elif '爪牙' not in characters:
    red_statement = f'，知道{characters.index('盲猎人') + 1}是盲猎人。\n'
for i in range(player_count):
    output_string += f'{i + 1}({player_names[i]})是{characters[i]}'
    match characters[i]:
        case '忠臣' | '公爵' | '大公' | '青年' | '捣蛋鬼':
            output_string += '。\n'
        case '爪牙' | '摩根勒菲':
            output_string += red_statement.format([red for red in reds if red != i + 1])
        case '牧师':
            output_string += f'，知道首任主持人是{'红' if starting_leader in cleric_sees else '蓝'}方。\n'
        case '盲猎人':
            if not director_cut or player_count >= 6:
                output_string += '。\n'
            else:
                output_string += f'，知道蓝方角色是{[x for x in ['牧师', '青年', '忠臣'] if x in characters]}。\n'
output_string += f'首任主持人是{starting_leader}。\n'
match player_count:
    case 4:
        output_string += '每次任务人数为2-3-2-3。\n'
    case 5:
        output_string += '每次任务人数为2-3-2-4-3。\n'
    case 6:
        output_string += '每次任务人数为2-3-4-3-4。\n'
    case 7:
        output_string += '每次任务人数为2-3-3-4-4。\n'
    case 8 | 9 | 10:
        output_string += '每次任务人数为3-4-4-5-5。\n'
if player_count >= 7 and not director_cut:
    output_string += '任务4需要2票失败才会失败。'
elif player_count >= 8 and director_cut:
    output_string += '任务3和4需要2票失败才会失败。'

st.subheader('分配结果')
st.write('请点击下方文本框右上角直接复制分配结果。')
st.code(output_string, language=None)