import json
import os


def base_url(course_name):
    return f"https://cdn13.git.ir/udemy/Udemy Docker and Kubernetes The Complete Guide-git.ir/{course_name}-git.ir.mp4"


with open('sections.json', 'r') as file:
    for section in json.load(file)['sections']:
        os.chdir(f'/media/Storage/Videos/DevOps/Docker and Kubernetes The Complete Guide/{section["name"]}')
        for course in section['courses']:
            os.system(f'wget -c --show-progress "{base_url(course)}"')
