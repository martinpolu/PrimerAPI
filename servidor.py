import uvicorn

def start_server(host="127.0.0.1",
                 port=50000,
                 num_workers=4,
                 loop="asyncio",
                 reload=False):
    uvicorn.run("WebServer:app",
                host=host,
                port=port,
                workers=num_workers,
                loop=loop,
                reload=reload)


