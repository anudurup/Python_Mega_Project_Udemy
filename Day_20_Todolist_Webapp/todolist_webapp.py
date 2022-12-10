import streamlit as st
import functions

# Run website with streamlit run <name of file with path>

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


# Order of creations of instances creates the order in the website.
st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase by productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:  # If we check the checkbox it will be True
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun() # This clears the task once it is checked.

st.text_input(label="", placeholder="Add new todo...", on_change=add_todo,
              key='new_todo')  # on_change adds a callback function

# print("Hello")  # This gets printed out for each reload the website.

# st.session_state  # prints the session dictionary on the web.
