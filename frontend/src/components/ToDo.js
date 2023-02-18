import React from 'react'
import { Link } from 'react-router-dom'


const ToDoItem = ({todo, deleteToDo}) => {
    return (
        <tr>
            <td>
                {todo.project.name}
            </td>
            <td>
                {todo.text}
            </td>
            <td>
                {todo.created}
            </td>
            <td>
                {todo.updated}
            </td>
            <td>
                {todo.user.username}
            </td>
            <td>
                {todo.active.toString()}
            </td>
            <td>
                <button onClick={()=>deleteToDo(todo.url)} type='button'>Delete</button>
            </td>
        </tr>
    )
}


const ToDoList = ({todoes, deleteToDo}) => {
    return (
        <div>
        <table>
            <th>
                Project 
            </th>
            <th>
                Text
            </th>
            <th>
                Time Created
            </th>
            <th>
                Time Updated
            </th>
            <th>
                User
            </th>
            <th>
                Status
            </th>
            {todoes.map((todo) => <ToDoItem todo={todo} deleteToDo={deleteToDo}/>)}
        </table>
        <Link to='/todoes/create'>Create</Link>
        </div>
    )
}


export default ToDoList