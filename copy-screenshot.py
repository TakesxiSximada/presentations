#! /usr/bin/env python
import os
import shutil


def main():
    screen_shot_dir = os.path.expanduser('~/Desktop')
    for filename in os.listdir(screen_shot_dir):
        if filename.startswith('screen'):
            src = os.path.join(screen_shot_dir, filename)
            dst = os.path.join('./images', filename.replace(' ', '-'))
            shutil.move(src, dst)



if __name__ == '__main__':
    main()
