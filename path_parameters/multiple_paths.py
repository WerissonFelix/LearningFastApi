from fastapi import FastAPI

app = FastAPI()

''' 
OpenAPI doesn't support a way to declare a path parameter to contain a 
path inside, as that could lead to scenarios that are difficult to
test and define.
'''
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    '''  
    In this case, the name of the parameter is file_path, and the last part,
    :path, tells it that the parameter should match any path.
    
    ex: input: /home/johndoe/myfile.txt
    
    returns: 
    {
        "file_path": "/home/johndoe/myfile.txt"
    }

    '''
    return {"file_path": file_path}



# If we put this path /home/johndoe/myfile.txt in this function:

@app.get('/files/{file_path}')
async def read_file(file_path: str):
    return {'file_path': file_path}

'''   

We get this result: 

{
    
  "detail": "Not Found"
}


'''
