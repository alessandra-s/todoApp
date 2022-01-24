"""   pytest
"""
from app import app

def test():
 """
 this function tests the flask application has a correct response code
    
 """
 response = app.test_client().get("/")
 assert response.status_code== 200

def test2():
 """
 this function tests the flask application has a correct response code
    
 """
 response = app.test_client().get("/edit")
 assert response.status_code== 200


def test3():
 """
 this function tests the flask application has a correct response code
    
 """
 response = app.test_client().get("/edit")
 assert b"To Do App" in response.data
 assert b"Todo Title" in response.data
 assert b"Add" in response.data

