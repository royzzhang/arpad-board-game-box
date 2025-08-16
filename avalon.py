import random

import streamlit as st

with st.sidebar:
    player_count = st.slider('玩家数', min_value=5, max_value=10, value=5, step=1)
    player_names = [''] * player_count
    for i in range(player_count):
        player_names[i] = st.text_input(f'玩家{i + 1}')

st.title('阿瓦隆发牌器')

st.write(f'当前玩家数：{player_count}')

add_lancelot = False
lancelot_variant = 1
add_lady = False
if player_count >= 7:
    st.subheader('可追加选项（需7人以上）')
    add_lancelot = st.checkbox('加入兰斯洛特')
    lancelot_variant = st.pills('选择兰斯洛特变种：', [1, 2, 3], default=1)
    add_lady = st.checkbox('加入湖中仙女')

characters = ['梅林', '派西维尔', '刺客', '莫甘娜']
swap_turns = []
if player_count in [7, 10] and not add_lancelot:
    characters.append('奥伯伦')
if (player_count == 9 and not add_lancelot) or player_count == 10:
    characters.append('莫德雷德')
if player_count == 8 and not add_lancelot:
    characters.append('爪牙')
if add_lancelot:
    characters += ['蓝兰斯洛特', '红兰斯洛特']
    if lancelot_variant == 2:
        swap_turns = [i + 1 for i, x in enumerate(random.sample([True, False], counts=[2, 4], k=5)) if x]
    elif lancelot_variant == 3:
        swap_turns = [i + 1 for i, x in enumerate(random.sample([True, False], counts=[2, 5], k=5)) if x]
while len(characters) < player_count:
    characters.append('忠臣')
random.shuffle(characters)

reds = merlin_sees = [characters.index('刺客') + 1, characters.index('莫甘娜') + 1]
if '奥伯伦' in characters:
    merlin_sees.append(characters.index('奥伯伦') + 1)
if '莫德雷德' in characters:
    reds.append(characters.index('莫德雷德') + 1)
if '爪牙' in characters:
    merlin_sees.append(characters.index('爪牙') + 1)
    reds.append(characters.index('爪牙') + 1)
if '红兰斯洛特' in characters:
    merlin_sees.append(characters.index('红兰斯洛特') + 1)
    if lancelot_variant == 1:
        reds.append(characters.index('红兰斯洛特') + 1)

output_string = ''

red_statement = '，和{}之间彼此知道是红方。\n'
if add_lancelot and lancelot_variant in [2, 3]:
    red_statement = red_statement[:-2] + f'，且知道{characters.index('红兰斯洛特') + 1}是初始红兰斯洛特。\n'

for i in range(player_count):
    output_string += f'{i + 1}({player_names[i]})是{characters[i]}'
    match characters[i]:
        case '梅林':
            output_string += f'，知道{merlin_sees}是红方。\n'
        case '派西维尔':
            output_string += f'，知道{sorted([characters.index('梅林') + 1, characters.index('莫甘娜') + 1])}其中一个是梅林而另一个是莫甘娜。\n'
        case '忠臣' | '奥伯伦':
            output_string += '。\n'
        case '刺客' | '莫甘娜' | '莫德雷德' | '爪牙':
            output_string += red_statement.format([red for red in reds if red != i + 1])
        case '蓝兰斯洛特':
            match lancelot_variant:
                case 1:
                    output_string += f'，知道{characters.index('红兰斯洛特') + 1}是红兰斯洛特。\n'
                case 2:
                    output_string += f'，与红兰斯洛特在任务{swap_turns}前交换身份，每次任务前宣布是否交换。\n'
                case 3:
                    if swap_turns:
                        output_string += f'，与红兰斯洛特在任务{swap_turns}前交换身份，游戏开始时宣布交换轮数。\n'
                    else:
                        output_string += f'，游戏开始时宣布两个兰斯洛特之间不会交换身份。\n'
        case '红兰斯洛特':
            match lancelot_variant:
                case 1:
                    output_string += (f'，知道{characters.index('蓝兰斯洛特') + 1}是红兰斯洛特' +
                                      red_statement.format([red for red in reds if red != i + 1]))
                case 2:
                    output_string += f'，与蓝兰斯洛特在任务{swap_turns}前交换身份，每次任务前宣布是否交换。\n'
                case 3:
                    if swap_turns:
                        output_string += f'，与蓝兰斯洛特在任务{swap_turns}前交换身份，游戏开始时宣布交换轮数。\n'
                    else:
                        output_string += f'，游戏开始时宣布两个兰斯洛特之间不会交换身份。\n'

starting_leader = random.choice(range(player_count)) + 1
output_string += f'首任主持人是{starting_leader}。\n'
if add_lady:
    output_string += f'首位湖中仙女是{starting_leader + 1 if starting_leader < player_count else 1}。\n'
match player_count:
    case 5:
        output_string += '每次任务人数为2-3-2-3-3。\n'
    case 6:
        output_string += '每次任务人数为2-3-4-3-4。\n'
    case 7:
        output_string += '每次任务人数为2-3-3-4-4。\n'
    case 8 | 9 | 10:
        output_string += '每次任务人数为3-4-4-5-5。\n'
if player_count >= 7:
    output_string += '任务4需要2票失败才会失败。'

st.subheader('分配结果')
st.write('请点击下方文本框右上角直接复制分配结果。')
st.code(output_string, language=None)
