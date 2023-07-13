#!/bin/bash

curl -X POST http://localhost:5000/api/timeline_post -d 'name=John Doe&email=johndoe@example.com&content=Testing the endpoints'
curl http://localhost:5000/api/timeline_post



