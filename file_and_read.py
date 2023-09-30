import os 
def paste_content(outputFile, content):
    with open(f'{outputFile}.py','a') as f:
        f.write(content)
        f.close()

def read_file(filename):
    with open(filename, 'r') as file:
        code = file.read()
    return code

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

def file_name(path):
    file_detail=os.path.basename(f'{path}').split('.')
    file_name_for_rename=file_detail[0][:-2]
    file_number=file_detail[0][-2::]
    os.chdir(r'C:/Users/Dell/Desktop/local_version')
    output(file_detail,file_name_for_rename,file_number,path)
input=r'C:\Users\Dell\Desktop\local_version/discord_message_main_01.py'
file_name(input)

