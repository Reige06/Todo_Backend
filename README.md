﻿# Todo_Backend
📌 Todo List API Endpoints
Base URL: https://bongo-todolistapp-backend.onrender.com/api/

✅ Tasks
Method	Endpoint	Description	Request Body
GET	/todos/	Get all tasks	❌ None
POST	/todos/	Create a new task	{ "description": "New Task", "status": "pending" }
GET	/todos/<id>/	Get a specific task by ID	❌ None
PATCH	/todos/<id>/	Update a task (edit description or status)	{ "description": "Updated Task" } or { "status": "completed" }
DELETE	/todos/<id>/	Delete a task	❌ None
🔥 Example API Calls
1️⃣ Fetch All Tasks
bash
Copy
Edit
curl -X GET https://bongo-todolistapp-backend.onrender.com/api/todos/
Response (JSON)

json
Copy
Edit
[
  { "id": 1, "description": "Buy groceries", "status": "pending" },
  { "id": 2, "description": "Complete homework", "status": "completed" }
]
2️⃣ Add a New Task
bash
Copy
Edit
curl -X POST https://bongo-todolistapp-backend.onrender.com/api/todos/ \
     -H "Content-Type: application/json" \
     -d '{"description": "Read a book", "status": "pending"}'
Response

json
Copy
Edit
{ "id": 3, "description": "Read a book", "status": "pending" }
3️⃣ Update a Task (Edit Description)
bash
Copy
Edit
curl -X PATCH https://bongo-todolistapp-backend.onrender.com/api/todos/3/ \
     -H "Content-Type: application/json" \
     -d '{"description": "Read a novel"}'
Response

json
Copy
Edit
{ "id": 3, "description": "Read a novel", "status": "pending" }
4️⃣ Mark Task as Completed
bash
Copy
Edit
curl -X PATCH https://bongo-todolistapp-backend.onrender.com/api/todos/3/ \
     -H "Content-Type: application/json" \
     -d '{"status": "completed"}'
Response

json
Copy
Edit
{ "id": 3, "description": "Read a novel", "status": "completed" }
5️⃣ Delete a Task
bash
Copy
Edit
curl -X DELETE https://bongo-todolistapp-backend.onrender.com/api/todos/3/
Response

json
Copy
Edit
{ "message": "Task deleted successfully" }
