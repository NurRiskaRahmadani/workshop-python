# Mencoba nilai string:
words = ['kucing', 'jendela', 'defenestrate']
for j in words:
    print(j, len(j))


# Membuat sampel koleksi
users = {'Mashiho': 'active', '김준규': 'inactive', 'ハルト': 'active'}

# Strategi: Mengulang salinan
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
        
# Strategi: Membuat koleksi baru
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

