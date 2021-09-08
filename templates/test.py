name = '김소은'
age = '22'

hello = f'제이름은{name}입니다. 나이는 {age}입니다.'

print(hello);

from datetime import datetime

today = datetime.now()
mytime = today.strftime('%Y년%m-%d-%H-%M-%S')

filename = f'file-{mytime}'

print(mytime)