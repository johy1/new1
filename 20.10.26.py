import requests as req

#GET
resGet=req.get("https://guides.github.com/activities/hello-world/#commit",params=None)

#POST
resPost=req.post("https://guides.github.com/activities/hello-world/#commit",data=None,json=None)
