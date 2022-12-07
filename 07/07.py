with open('07/input.txt') as f:
    lines = [line.strip('\n') for line in f];

fs = {};
currentDir = '';
for line in lines:
    line = line.split(" ");
    match line[0]:
        case '$':
            match line[1]:
                case 'cd':
                    if line[2] == '/':
                        currentDir = '';
                    elif line[2] == '..':
                        currentDirArr = currentDir.split('/')
                        currentDirArr.pop();
                        currentDir = '/'.join(currentDirArr);
                    else:
                        currentDir += '/' + line[2];
                case 'ls':
                    continue;
        case 'dir': 
            continue;
        case _:
            size = int(line[0]);
            file = line[1];
            fs[currentDir + '/' + file] = size;


directories = {}
for entry in fs:
    entryDirs = entry.split('/');
    while(entryDirs):
        elem = entryDirs.pop()
        if elem == '':
            break;
        if '/'.join(entryDirs) in directories:
            directories['/'.join(entryDirs)] += fs[entry];
        else:
            directories['/'.join(entryDirs)] = fs[entry];
        
# print(directories);

#7a: 
print('7a:', sum((filter(lambda elem: elem < 100000, directories.values()))));

#7b:
totalSpace = directories[''];
freeSpace = 70000000 - totalSpace;
if freeSpace < 30000000:
    requiredSpace = 30000000 - freeSpace;
    filteredDir = dict(filter(lambda elem: elem[1] > requiredSpace, directories.items()));
    print('7b:', min(filteredDir.values()))


