from collections import deque

# this is more into the collections series better to surface off the collections and file operation first before
# jumping into the below program


# find the line with the words and append it to the deque
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# example of usage of file
if __name__ == '__main__':
    with open('python.txt') as f:
        for lines, prevlines in search(f, 'Python', 4):
            for pline in prevlines:
                print(pline, end='')
            print(lines, end='')
            print('_'*20)
