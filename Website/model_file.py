
from imageai.Detection import ObjectDetection
import os
import json

list_of_animals = ["bird",   "cat",   "dog",   "horse",   "sheep",   "cow",   "elephant",   "bear",   "zebra", "giraffe"]

def count_humans(list_of_dicts):
    count = 0
    for each in list_of_dicts:
        if each["name"]=="person":
            count+=1
    return count

def count_animals(list_of_dicts):
    count = 0
    for each in list_of_dicts:
        if each["name"] in list_of_animals:
            count+=1
    return count

def count_objects(list_of_dicts):
    count = 0
    for each in list_of_dicts:
        if each["name"] not in list_of_animals and each["name"] != "person" :
            count+=1
    return count

def execute_model_all (file_name) :
    execution_path = os.getcwd()
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    detections=detector.detectObjectsFromImage(input_image=os.path.join(execution_path , file_name), output_image_path=os.path.join(execution_path , "image_detected.jpg"))
    
    count_of_humans = count_humans(detections)
    count_of_animals = count_animals(detections)
    count_of_objects = count_objects(detections)

    D_humans = {"name":"humans","count":count_of_humans}
    D_animals = {"name":"animals","count":count_of_animals}
    D_objects = {"name":"objects","count":count_of_objects}

    lst_of_json_objects = []
    lst_of_json_objects.append(json.dumps(D_humans))
    lst_of_json_objects.append(json.dumps(D_animals))
    lst_of_json_objects.append(json.dumps(D_objects))

        
    return lst_of_json_objects
