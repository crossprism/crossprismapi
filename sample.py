from urllib import request
import json
import shutil

classifierUrl = "http://localhost:9000/classify"

def processJPEGImage(imgdata,treepath = "default"):
    req = request.Request(classifierUrl, data=imgdata, method="POST")
    req.add_header('Content-Type', 'image/jpeg')
    req.add_header('X-Classifier-Tree', treepath)
    with request.urlopen(req) as f:
        content = f.read()
        results = json.loads(content)
        return results['scores']
    
with open('test.jpg','rb') as f:
    imgdata = f.read()
    scores = processJPEGImage(imgdata)
    print(scores)    
