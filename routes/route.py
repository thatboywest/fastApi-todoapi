from fastapi import APIRouter
from models.todos import Todo
from config.database import collection_name
from schema.schema import list_serial
from bson import ObjectId
router = APIRouter()

@router.get("/")
async def get_todos():
   todos=list_serial(collection_name.find())
   return todos
@router.post("/")
async def post_todos():
   collection_name.insert_one(dict(todos))