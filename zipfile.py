import zipfile

def unzip(dataset):
    print('downlaoding files....')
    if not os.path.exists('egohands'):
        with zipfile.ZipFile(dataset,'r') as uz:
            uz.extractall('egohands')
            print('Done !')
            uz.close()) 
