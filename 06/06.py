with open('06/input.txt') as f:
    lines = [line.strip('\n') for line in f];
#6a:
for line in lines:
    line = [*line];
    print(line)
    i = 0;
    while(i < len(line)):
        if len(set(line[i:i+4])) == 4:
            print(line[i:i+4])
            print(i+4);
            break;
        i+= 1;
#6b:
for line in lines:
    line = [*line];
    print(line)
    i = 0;
    while(i < len(line)):
        if len(set(line[i:i+14])) == 14:
            print(line[i:i+14])
            print(i+14);
            break;
        i+= 1;