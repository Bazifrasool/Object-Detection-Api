--------------------README------------------
1.Pre-requisites
2.How To Launch
3.Notes
--------------------------------------------
----------------Pre-requisites--------------
The code has been tested to work with the following libraries,
which are required to run it:
1.tensorflow==1.13.1
2.keras==2.3.1
3.json
4.flask==1.1.1
5.werkzeug==1.0.0
6.opencv==3.4.1
7.imageai
----------------How-To-Launch--------------

Extract Model_Compressed into the Website directory
(This was do circumvent 100MB size limit of Github)

1.Launch api.py to run in the backgroud and 
ensure to run from current working directory.
2. Open Index.html in your browser
3.Select file to upload for Object detection
4.Submit
5.Detected_objects.json has json object data and,
  Json data is displayed
----------------Notes--------------
Creates a json file so needs write access.
May not work correctly on updated version of libraries
Uses RESnet Model and Supported Classes of Detected_objects are:

    person,   bicycle,   car,   motorcycle,   airplane,
    bus,   train,   truck,   boat,   traffic light,   fire hydrant,   stop_sign,
    parking meter,   bench,   bird,   cat,   dog,   horse,   sheep,   cow,   elephant,   bear,   zebra,
    giraffe,   backpack,   umbrella,   handbag,   tie,   suitcase,   frisbee,   skis,   snowboard,
    sports ball,   kite,   baseball bat,   baseball glove,   skateboard,   surfboard,   tennis racket,
    bottle,   wine glass,   cup,   fork,   knife,   spoon,   bowl,   banana,   apple,   sandwich,   orange,
    broccoli,   carrot,   hot dog,   pizza,   donot,   cake,   chair,   couch,   potted plant,   bed,
    dining table,   toilet,   tv,   laptop,   mouse,   remote,   keyboard,   cell phone,   microwave,
    oven,   toaster,   sink,   refrigerator,   book,   clock,   vase,   scissors,   teddy bear,   hair dryer,
    toothbrush
    
Bazif Rasool
dt:04-03-2020