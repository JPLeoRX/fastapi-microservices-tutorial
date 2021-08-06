# Run migrations
from database import migration
migration()

# Run dependency injections
import os
import library_utils
from injectable import load_injection_container
load_injection_container()
load_injection_container(str(os.path.dirname(library_utils.__file__)))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from resources.resource_ping import router_ping
from resources.resource_book import router_book

app = FastAPI()

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup all resources
app.include_router(router_ping)
app.include_router(router_book)
