#max points [4]
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse("/docs")

"""
1. Create a GET endpoint '/hello' that give as response: "Hello!".
2. Show the result from swagger (start the application, a browser will be appaired)
3. copy the curl command
4. paste the command here: #CURL COMMAND
"""

# code goes here


if __name__ == "__main__":
  # keep this code call here 
  import uvicorn
  config = uvicorn.Config("p_ex05:app", port=5000, log_level="info")
  server = uvicorn.Server(config)
  server.run()

