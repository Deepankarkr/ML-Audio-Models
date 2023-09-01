import base64
import json
import requests
import sys
import tensorflow as tf

x = tf.io.read_file(sys.argv[1])
b64str = base64.urlsafe_b64encode(x.numpy()).decode("utf-8")

data = json.dumps({"signature_name": "serving_default", "instances": [b64str]})

headers = {"content-type": "application/json"}
json_response = requests.post(
            "http://localhost:8501/v1/models/default/versions/1:predict", data=data, headers=headers
            )
#print(json.loads(json_response.text))

import numpy as np
class_to_number = {0 : 1,  1 : 10,  2 : 100,  3 : 11,  4 : 12,  5 : 13,  6 : 14,  7 : 15,  8 : 16,  9 : 17,  10 : 18,  11 : 19,  
                   12 : 2,  13 : 20,  14 : 21,  15 : 22,  16 : 23,  17 : 24,  18 : 25,  19 : 26,  20 : 27,  21 : 28,  22 : 29,  
                   23 : 3,  24 : 30,  25 : 31,  26 : 32,  27 : 33,  28 : 34,  29 : 35,  30 : 36,  31 : 37,  32 : 38,  33 : 39,  
                   34 : 4,  35 : 40,  36 : 41,  37 : 42,  38 : 43,  39 : 44,  40 : 45,  41 : 46,  42 : 47,  43 : 48,  44 : 49,  
                   45 : 5,  46 : 50,  47 : 51,  48 : 52,  49 : 53,  50 : 54,  51 : 55,  52 : 56,  53 : 57,  54 : 58,  55 : 59,  
                   56 : 6,  57 : 60,  58 : 61,  59 : 62,  60 : 63,  61 : 64,  62 : 65,  63 : 66,  64 : 67,  65 : 68,  66 : 69,  
                   67 : 7,  68 : 70,  69 : 71,  70 : 72,  71 : 73,  72 : 74,  73 : 75,  74 : 76,  75 : 77,  76 : 78,  77 : 79,  
                   78 : 8,  79 : 80,  80 : 81,  81 : 82,  82 : 83,  83 : 84,  84 : 85,  85 : 86,  86 : 87,  87 : 88,  88 : 89,  
                   89 : 9,  90 : 90,  91 : 91,  92 : 92,  93 : 93,  94 : 94,  95 : 95,  96 : 96,  97 : 97,  98 : 98,  99 : 99}
print(class_to_number(np.argmax(np.array((json.loads(json_response.text)["predictions"][0])))))