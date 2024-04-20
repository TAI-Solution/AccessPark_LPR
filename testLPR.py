from fastapi import FastAPI, HTTPException, Request

app = FastAPI()

# POST route
@app.post("/iclock/cdata")
async def create_item(request: Request):
    # Get the JSON body directly from the request
    data = await request.json()

    print(data)

    # return the received data
    return data
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)