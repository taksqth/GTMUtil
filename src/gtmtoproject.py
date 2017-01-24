# -*- coding: utf-8 -*-

import os
import sys
import json

def create_project(container_filename):
    gtm_obj = {}

    with open(container_filename) as container_file:
        gtm_obj = json.load(container_file)
    html_tag_list = [tag for tag in gtm_obj["containerVersion"]["tag"] if tag["type"] == "html"]

    if not os.path.exists(path_to_project):
        # WARNING: Isso é uma condição de corrida não tratada
        os.makedirs(path_to_project)
        
    for html_tag in html_tag_list:
        with open(path_to_project + '/' + html_tag["name"] + ".html", "w") as html_file:
            html_file.write(html_tag["parameter"][0]["value"])

def compile_project(container_filename):
    gtm_obj = {}

    with open(container_filename) as container_file:
        gtm_obj = json.load(container_file)

    if not os.path.exists(path_to_project):
        print("Não existe um projeto de GTM na pasta atual. Abortando...")
        sys.exit(1)
    filenames_in_project = os.listdir(path_to_project)

    for filename in [name for name in filenames_in_project if name.endswith(".html")]:
        with open(path_to_project + '/' + filename) as html_file:
            html_tag = next(tag for tag in gtm_obj["containerVersion"]["tag"] if tag["name"] == filename.split('.')[0])
            html_tag["parameter"][0]["value"] = html_file.read()

    with open(container_filename, 'w') as container_file:
        json.dump(gtm_obj, container_file, indent=4)

if __name__ == "__main__":
    path_to_project = "project/"

    if len(sys.argv) < 2:
        print("Você precisa especificar um comando")
        sys.exit(1)

    if sys.argv[1] == "init":
        if len(sys.argv) < 3:
            print("Você precisa especificar um arquivo de container do GTM")
            sys.exit(1)
        create_project(sys.argv[2])
    elif sys.argv[1] == "compile":
        if len(sys.argv) < 3:
            print("Você precisa especificar um arquivo de container do GTM")
            sys.exit(1)
        compile_project(sys.argv[2])
    else:
        print("Comando desconhecido")
        sys.exit(1)
