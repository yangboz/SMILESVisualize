import uvicorn
from fastapi import FastAPI, File, UploadFile
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware




app_desc = """<h2>Try this app by demostrating[a,b,c,d,e] data and index  for `api/res`</h2>
<h2>Try get/add/modify/delete rest functions and verify return response </h2>
<br>by Aniket Maurya"""

app = FastAPI(title='restful FastAPI Starter Pack', description=app_desc)

app.data = ['a','b','c','d']

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse(url="/docs")

@app.get("/api/res")
def get_data():
    return app.data
@app.post("/api/res")
def add_data(index:int,value:str):
    app.data.insert(index,value)
    return app.data

@app.put("/api/res")
def modify_data(index:int,value:str):
    app.data[2]
    return app.data

@app.delete("/api/res")
def delete_data(index:int):
    return app.data


if __name__ == "__main__":
    uvicorn.run(app, debug=True)
