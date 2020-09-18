class errorRecord:
    def __init__(self, path, line_num):
        self.path = path
        self.line_num = line_num
        self.fileName = getFileNameByPath(path)
        self.fullName = getFullFileNameByPath(path)

s = input()
def getFullFileNameByPath(path):
    return path.split('\\')[-1]

def getFileNameByPath(path):
    return path.split('\\')[-1][:16]
paths = []
while s:
    path, line_num = s.split(' ')
    paths.append(path)


