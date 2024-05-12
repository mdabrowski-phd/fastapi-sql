from pydantic import BaseModel
from enum import Enum


# Tasks
class TaskBody(BaseModel):
    description: str
    priority: int | None = None
    is_complete: bool = False


class TaskResponse(BaseModel):
    id_: int
    description: str
    priority: int | None = None
    is_complete: bool = False


class GetSingleTaskResponse(BaseModel):
    result: TaskResponse


class GetAllTasksResponse(BaseModel):
    result: list[TaskResponse]


class PostTaskResponse(BaseModel):
    message: str
    details: TaskResponse


class PostTaskNoDetailResponse(BaseModel):
    message: str


class PutTaskResponse(BaseModel):
    message: str
    new_value: TaskResponse


# Users
class UserBody(BaseModel):
    username: str
    password: str
    is_admin: bool = False


class UserResponse(BaseModel):
    id_: int
    username: str
    password: str
    is_admin: bool = False


class GetSingleUserResponse(BaseModel):
    result: UserResponse


class GetAllUsersResponse(BaseModel):
    result: list[UserResponse]


class PostUserResponse(BaseModel):
    message: str
    details: UserResponse


class PutUserResponse(BaseModel):
    message: str
    new_value: UserResponse


class PutUserNoDetailResponse(BaseModel):
    message: str


# Utils
class SortOrders(Enum):
    ASCENDING = "asc"
    DESCENDING = "desc"


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: int
