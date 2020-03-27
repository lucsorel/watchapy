from fastapi import FastAPI
from watchapy.watchapy import watchapy
testapp = FastAPI()

@testapp.get('/')
@watchapy()
def read_root():
    return {'Hello': 'World'}
