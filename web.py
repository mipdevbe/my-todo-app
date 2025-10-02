import functions
import streamlit as st

functions.check_todos_exists()
todos = functions.load_todos()

def add_todo():
    todo = st.session_state["new_todo"].strip()
    if len(todo) > 0:
        todos.append(todo)
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todo_to_complete = todos[index]
        todos.remove(todo_to_complete)
        functions.write_todos(todos)
        del st.session_state[todo_to_complete]
        st.rerun()

st.text_input(label="Enter a todo:", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")

#st.session_state
