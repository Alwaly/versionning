import os
import nbformat as nbf
import subprocess


def git_executer(cmd):
    for i in cmd:
        resultat = subprocess.run(i, capture_output=True, text=True, shell=True)

    if resultat.returncode == 0:
        print("La commande Git s'est exécutée avec succès.")
        print("Sortie de la commande :")
        print(resultat.stdout)
    else:
        print("La commande Git a rencontré une erreur.")
        print("Erreur de la commande :")
        print(resultat.stderr)

def write_notebook(file_name:str, source_code:str):
    notebook = nbf.v4.new_notebook()

    code = nbf.v4.new_code_cell(source=source_code)
    notebook['cells'].append(code)
    nbf.write(notebook, file_name)


def create_folder(name: str):
    os.mkdir(name)

def create_file(name: str, content=""):
    fd = os.open(name, os.O_RDWR|os.O_CREAT)
    os.write(fd, content.encode())

def create_first_rank_file():
     for file in files:
        create_file(file)

def create_first_rank_folder_subfolders_and_subfiles():
     for i in range(len(folders_names)):
        create_folder(folders_names[i]['folder']["nom"])
        try:
            for k in folders_names[i]['folder']["subfolder"]:
                create_folder(os.path.join(folders_names[i]['folder']["nom"], k))
        except:
            try:
                for file in folders_names[i]['folder']["file"]:
                    create_file(os.path.join(folders_names[i]['folder']["nom"], file))
            except:
                continue
my_code="""import os

def create_folder(name: str):
    os.mkdir(name)

def create_file(name: str, content=""):
    fd = os.open(name, os.O_RDWR|os.O_CREAT)
    os.write(fd, content.encode())

def create_first_rank_file():
     for file in files:
        create_file(file)

def create_first_rank_folder_subfolders_and_subfiles():
     for i in range(len(folders_names)):
        create_folder(folders_names[i]['folder']["nom"])
        try:
            for k in folders_names[i]['folder']["subfolder"]:
                create_folder(os.path.join(folders_names[i]['folder']["nom"], k))
        except:
            try:
                for file in folders_names[i]['folder']["file"]:
                    create_file(os.path.join(folders_names[i]['folder']["nom"], file))
            except:
                continue

folders_names = [
                    {"folder":{"nom":"data", "subfolder":["cleaned", "raw"]}},
                      {"folder":{"nom":"docs"}}, 
                      {"folder":{"nom":"models"}},
                      {"folder":{"nom":"notebooks","file":["main_notebook.ipynb"]}}, 
                      {"folder":{"nom":"reports"}},
                      {"folder":{"nom":"src","file":["utils.py"]}}
                    ]
files = ['license', 'makefile']
if __name__=="__main__":
   create_first_rank_folder_subfolders_and_subfiles()
   create_first_rank_file()"""



folders_names = [
                    {"folder":{"nom":"data", "subfolder":["cleaned", "raw"]}},
                      {"folder":{"nom":"docs"}}, 
                      {"folder":{"nom":"models"}},
                      {"folder":{"nom":"notebooks","file":["main_notebook.ipynb"]}}, 
                      {"folder":{"nom":"reports"}},
                      {"folder":{"nom":"src","file":["utils.py"]}}
                    ]
files = ['license', 'makefile']

if __name__=="__main__":
    create_first_rank_folder_subfolders_and_subfiles()
    create_first_rank_file()
    create_file("src/utils.py", my_code)
    write_notebook("notebooks/main_notebook.ipynb", my_code)
    git_executer(['git init'])