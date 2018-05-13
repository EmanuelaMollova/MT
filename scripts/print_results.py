import pickle
import os.path
import numpy as np

map = {
    'public transport':            'transport',
    'driving':                     'driving',
    'walking outdoor':             'walking out',
    'walking indoor':              'walking in',
    'biking':                      'biking',
    'having drinks with somebody': 'drinks smbd',
    'having drinks/meal alone':    'dr/m alone',
    'having meal with somebody':   'meal smbd',
    'socializing':                 'socializing',
    'attending a seminar':         'seminar',
    'meeting':                     'meeting',
    'reading':                     'reading',
    'tv':                          'television',
    'cleaning and chores':         'cleaning',
    'working':                     'working',
    'cooking':                     'cooking',
    'shopping':                    'shopping',
    'talking':                     'talking',
    'resting':                     'resting',
    'mobile':                      'mobile',
    'plane':                       'plane',
}

def print_prediction(label, percent):
    label = map[label.decode('UTF-8')]
    percent = str(round(percent * 100, 1)) + '%'

    return '<td>' + label + '<strong>' + percent + '</strong></td>'

def print_img_td(img_path):
    img_path = img_path.replace('../../..', '/home/emanuela/caffe-docker')
    return '<td><img src="'+img_path+'"></td>'

def get_results(results_path):
    pkl_file = open(results_path, 'rb')
    results  = pickle.load(pkl_file, encoding='latin1')
    pkl_file.close()

    return results

def collect_info(results):
    n = 6
    collection = [[] for _ in range(n)]
    correct = []
    for res in results:
        if (res['label'] != res['result'][0][0]):
            collection[0].append(print_img_td(res['image']))
            for i in range(0, 5):
                collection[i+1].append(print_prediction(res['result'][i][0], res['result'][i][1]))
        else:
            correct.append(print_img_td(res['image']))

    imgs_info = str(len(results)) + ' images total, ' + str(len(correct) / len(results) * 100) + '% correct (' + str(len(correct)) + ' correct, ' + str(len(collection[0])) + ' incorrect)'

    new_collection = []
    for coll in collection:
        new_collection.append([coll[i:i + chunk_size] for i in range(0, len(coll), chunk_size)])

    correct_table_body = ''
    correct = [correct[i:i + chunk_size] for i in range(0, len(correct), chunk_size)]
    for c in correct:
        correct_table_body += '<tr>'+''.join(c) + '</tr>'

    incorrect_table_body = ''
    for i in range(0, len(new_collection[0])):
        for c in new_collection:
            incorrect_table_body += '<tr>'+''.join(c[i]) + '</tr>'


    return {
        'imgs_info': imgs_info,
        'correct_table_body': correct_table_body,
        'incorrect_table_body': incorrect_table_body,
    }

def write_results(category, results, template_path, output_path):
    with open(template_path, 'r') as tmpl_file:
        tmpl = tmpl_file.read()

    tmpl = tmpl.replace("CATEGORY", category)
    tmpl = tmpl.replace("IMAGES INFO", results['imgs_info'])
    tmpl = tmpl.replace("INCORRECT TABLE BODY", results['incorrect_table_body'])
    tmpl = tmpl.replace("CORRECT TABLE BODY", results['correct_table_body'])

    with open(output_path + category + '.html', "w") as text_file:
        text_file.write(tmpl)


if __name__ == "__main__":
    experiment_name = 'user3_unseen'

    chunk_size = 12
    template_path = '/home/emanuela/caffe-docker/results.html'
    results_path  = '/home/emanuela/caffe-docker/notebooks/emanuela/activity-recognition/models/finetuning-googlenet/' + experiment_name + '/results_by_category/'

    labels_path = '/home/emanuela/caffe-docker/data/emanuela/activity-recognition/labels/labels.txt'
    labels = list(np.loadtxt(labels_path, str, delimiter='\n'))
    output_names = [str(i) + '_' + label.replace('/', '_').replace(' ', '_') for i, label in enumerate(labels)]

    for name in output_names:
        if os.path.isfile(results_path + name + '_outfile'):
            results = get_results(results_path + name + '_outfile')
            info = collect_info(results)
            write_results(name, info, template_path, results_path)
