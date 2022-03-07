import os

if __name__ == '__main__':

    print("hello world")
    f = open('a.txt', 'r')
    for i in f:
        os.system('hexo n ' + i + '.txt')

