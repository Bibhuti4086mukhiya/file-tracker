# import time
# import schedule

# def my_task():
#     Your task logic here
import os
def read_file(location_file,fileName):
    os.chdir(location_file)
    print(os.getcwd())
    with open(fileName +'.py', 'r') as file:
        code = file.read()
    return code

def paste_content(new_folder_loc,first_name,content):
    os.chdir(new_folder_loc)
    with open(f'{first_name}.py','a') as f:
        f.write(content)
        f.close()

def output(file_detail,file_name_for_rename,file_number,path):
    try:
        if type(int(file_number))==int:
            incr=int(file_number)+1
            num='{0:02}'.format(incr)
            file_new_name=file_name_for_rename+f'{num}'
            read_content=read_file(path)
            print(os.getcwd(),read_content)
            paste_content(file_new_name,read_content)
            
    except:
        first_name=file_detail[0]+'_01'
        read_content=read_file(path)
        paste_content(first_name,read_content)

def first_name_file(fileName,location_file,location):
    read_content=read_file(location_file,fileName)
    return read_content


def create_folder(path,location_file,fileName):
    location=r'C:/Users/Dell/Desktop/local_version'
    for root, dirs, files in os.walk(location):
        break_break=False
        for i in dirs:
            if fileName==i:
                print('found')
                break_break=True
        if break_break==True:
            break
    else:
        os.chdir(location)
        os.mkdir(fileName)
        new_folder_loc=location+"/"+fileName+"/"
        content=first_name_file(fileName,location_file,location)
        first_name=fileName+'_01'
        paste_content(new_folder_loc,first_name,content)
        os.system('git init')
        os.system('git add .')
        os.system("""git commit -m "first commit" """)

def main(path):
    file_name=os.path.basename(f'{path}').split('.')
    location_of_file=os.path.split(f'{path}')
    create_folder(path,location_file=location_of_file[0],fileName=file_name[0])

input=r'C:\Users\Dell\Desktop\storage\timeline\2023\july\auto access relate code\main.py'
main(input)

# Schedule the task to run after 1 hour
# schedule.every(1).hours.do(my_task)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
