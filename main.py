import os,sys


def Init():
    """초기화:기본 매시지 출력, 변수초기화등등"""
    print("CNP")
    print("CLI NOTEPAD")
    print("*caution*")
    print("Currently only the .txt extension is available.")
    reqFolderPath_var=reqFolderPath()
    dir_path=reqFolderPath_var[0]
    dir_list=reqFolderPath_var[1]
    print(f"path:{dir_path}\nlist:{dir_list}")
    return [dir_path,dir_list]

def reqFolderPath():
    """폴더경로 받기, 변수에 저장"""
    try:
        folder_path = input("Please enter the path to the folder to open.")
        # if folder_path=="/:/EXIT":
        #     sys.exit(0)
        if os.path.exists(folder_path):
            pass
        else:
            raise FileNotFoundError(f"{folder_path} 경로가 존재하지 않습니다.")
        folderList=os.listdir(folder_path)
    except:
        print("The path you entered does not exist.\nPlease check for typos and re-enter.")
        reqFolderPath()
    else:
        return [folder_path,folderList]
    
def chooseEditFile():
    """수정할 파일경로 출력,입력받기"""
    global editPath,editList
    i=0
    for list in editList:
        i+=1
        print(f"{i}:{list}")
    while True:
        try:
            editFileNum=int(input("Please enter the number of the file to be modified."))
        except:
            print(f"Please enter a number greater than or equal to 1 and less than or equal to {i}.")
            continue
        else:
            if editFileNum+1>i:
                print(f"Please enter a number greater than or equal to 1 and less than or equal to {i}.")
            else:
                break
    editFile=editList[editFileNum-1]
    print(editFile)
    return editFile

        
    
# 실행, 변수선언
variables=Init()
editPath=variables[0]
editList=variables[1]
chooseEditFile()

