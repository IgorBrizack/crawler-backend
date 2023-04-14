import uvicorn

if __name__ == "__main__":
    uvicorn.run("server.app:app", host="https://crawler-challenge-backend.onrender.com", port=8000, reload=True)
