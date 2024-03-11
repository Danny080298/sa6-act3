string = ['apple','shoe','door','tv','desk','wallpaper']

new_list = sorted(string, key= lambda x:(len(x),x))
print(new_list)
