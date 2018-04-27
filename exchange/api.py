import os
import sys
import django

sys.path.append('/Users/Mitchell/PycharmProjects/mysite/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
django.setup()

import requests
from exchange.models import Course

r1 = requests.get('https://streamer.oit.duke.edu/curriculum/list_of_values/fieldname/SUBJECT?access_token=768f999413365b0cf3afdf1324d6e663')
subjects = r1.json()['scc_lov_resp']['lovs']['lov']['values']['value']
count = 0

for sub in subjects:    # keys = 'code', 'desc'
    if count >= 100:
        break

    query = sub['code'] + '%20-%20' + '%20'.join(sub['desc'].strip().split())
    request_url = r'https://streamer.oit.duke.edu/curriculum/courses/subject/' + query + r'?access_token=768f999413365b0cf3afdf1324d6e663'
    r2 = requests.get(request_url)
    if r2.status_code == 404 or int(r2.json()['ssr_get_courses_resp']['course_search_result']['ssr_crs_srch_count']) == 0:   # 404 error
        continue
    courses = r2.json()['ssr_get_courses_resp']['course_search_result']['subjects']['subject']['course_summaries']['course_summary']
    if isinstance(courses, dict):   # only one class for the subject
        c = Course(title=courses['course_title_long'], code=courses['subject']+courses['catalog_nbr'])
        c.save()
        count += 1
    else:
        c = Course(title=courses[0]['course_title_long'], code=courses[0]['subject'] + courses[0]['catalog_nbr'])
        c.save()
        count += 1
        '''
        for course in courses:  # keys = 'course_title_long', 'catalog_nbr'
            c = Course(title=course['course_title_long'], code=course['subject']+course['catalog_nbr'])
            c.save()
        '''