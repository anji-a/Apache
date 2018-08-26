import os,sys


def getFilePath(filename):
    rootdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    for folder, subs, files in os.walk(rootdir):
        if os.path.exists(os.path.join(folder, '__pycache__')):
            for fname in files:
                if os.path.splitext(fname)[0] == filename:
                    filelocation = os.path.abspath(os.path.join(folder, fname))
                #if os.path.splitext(filename)[1] == '.py' or os.path.splitext(filename)[1] == '.pyc':
                 #   if os.path.splitext(filename)[1] == '.py':
                 #       file_paths.append(filename)
                 #       modifiedtime = os.path.getmtime(os.path.abspath(os.path.join(folder, filename)))
                 #      file_dic[filename] = [filename, os.path.abspath(os.path.join(folder, filename)),
                 #                             os.path.splitext(filename)[1], modifiedtime, folder]
                        # print(file_dic)

    return filelocation