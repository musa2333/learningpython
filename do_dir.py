import os
def find_file(initial_path):
    for i in os.listdir(initial_path):
        if os.path.isfile(os.path.join(initial_path,i)):
            if 'test' in os.path.split(i)[1]: 
            	print(i)

        else:
            find_file(os.path.join(initial_path,i))

find_file(os.getcwd())

