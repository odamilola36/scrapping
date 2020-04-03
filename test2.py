import os
from datetime import datetime

start = datetime.now()
with open(os.path.join(os.path.join("C:\\Users\\odami\\developments\\bs4\\outputs"), "filename.txt"), "w", encoding= "utf-8") as file:
    toFile = 'we are writing this'
    file.write(toFile)

end = datetime.now()

print(end-start)