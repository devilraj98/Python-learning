import shutil
import datetime
import os

def backup_files(source,destination):
    today =datetime.datetime.today()
    backup_file_name = os.path.join(destination,f"{today}.tar.gz")
    shutil.make_archive(backup_file_name,'gztar',source)


sources = "/home/neeraj/Downloads/Python-Learning"    
destination = "/home/neeraj/Downloads/Python-Learning/backups"


backup_files(sources, destination)

