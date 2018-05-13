"""
Change the path to the directory where the images are located
"""

from helpers import *

def rewrite_paths_in_file(new_path, input_path, output_path):
    new_lines = []
    with open(input_path) as f:
        for line in f.readlines():
            line = line.strip()
            activity = extract_activity(line)
            img_name = extract_image_name(line, True)
            new_name = rewrite_path_in_img_name(new_path, img_name)

            new_lines.append("%s %s" % (new_name, activity))

    file = open(output_path, 'w')
    file.write("\n".join(new_lines))

if __name__ == "__main__":
    new_path    = '../../../data/emanuela/activity-recognition/images/NTCIR-Lifelog-256'
    input_path  = '/home/emanuela/caffe-docker/data/emanuela/activity-recognition/labels/user3_unseen/train.txt'
    output_path = '/home/emanuela/caffe-docker/data/emanuela/activity-recognition/labels/user3_unseen/train.txt'

    print("Replacing directory path with '%s' from %s to %s" % (new_path, input_path, output_path))

    rewrite_paths_in_file(new_path, input_path, output_path)
