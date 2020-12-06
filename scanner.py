import textract
import glob
import json

all_files = []

# loop over all files in the folder.
# (I put all the files in one folder).
for filepath in glob.iglob('/user/Desktop/all-files/*.*'): #(Can be: pdf, jpg, xls, xlsx, doc, docx)
    try:
        file_name = filepath.split('/')[len(filepath.split('/'))-1]
        text = textract.process(filepath).decode('utf-8', 'ignore')
        all_files.append({"name": file_name,"content": text})
        
        print(file_name + "\n")
    except:
        pass
    
def save():
    global all_files
    j = json.dumps(all_files)
    file = open("datalist.json", "w") 
    file.write(j) 
    file.close()
save()
