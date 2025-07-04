# SMILES need colorful visualization?
 oe with a python fastapi   restful template for sharing simplified Molecular input line entry system.

  examples: 
SMILE text:  OCCc1c(C)[n+](cs1)Cc2cnc(C)nc2N

visualize:
![vitamin](https://github.com/yangboz/SMILESVisualize/blob/master/SMILES_vitamin.jpeg)

## how to verify it?
```
pip install -r requirements.txt

```

## quick start


```
uvicorn application.server.main:app
```
then check http://localhost:8000/docs#
# docker

```
docker run -p 80:80 smartkit/fastapi-restful-starter
```

###SMILES

https://en.wikipedia.org/wiki/Simplified_Molecular_Input_Line_Entry_System

### need more complex,high resolution ?

drop email to youngwelle@gmail.com
