def get_activities():
    """Return the predefined 21 activities as a dictionary."""
    return {
        0:  'Public transport',
        1:  'Driving',
        2:  'Walking outdoor',
        3:  'Walking indoor',
        4:  'Biking',
        5:  'Having drinks with somebody',
        6:  'Having drinks/meal alone',
        7:  'Having meal with somebody',
        8:  'Socializing',
        9: 'Attending a seminar',
        10: 'Meeting',
        11: 'Reading',
        12: 'Tv',
        13: 'Cleaning and chores',
        14: 'Working',
        15: 'Cooking',
        16: 'Shopping',
        17: 'Talking',
        18: 'Resting',
        19: 'Mobile',
        20: 'Plane',
    }

def extract_activity(line):
    """
    Return as an integer the activity from a line in a file with annotated
    images.
    """
    return int(line.split(" ")[-1])

def extract_image_name(line, full_path=False):
    """
    Return the image file name from a line in a file with annotated images.
    If full_path is True, return the whole path to the image file.
    """
    name = line.split(" ")[:-1]
    name = ' '.join(name).strip()
    if '/' in name and not full_path:
        name = name.split('/')[-1]

    return name

def rewrite_path_in_img_name(new_dir, img_name, last_dirs_to_keep = 3):
    """Rewrite the path to the image file."""
    name_parts = img_name.split('/')
    name_parts = name_parts[-last_dirs_to_keep:]

    if new_dir:
        name_parts.insert(0, new_dir)

    return '/'.join(name_parts)
