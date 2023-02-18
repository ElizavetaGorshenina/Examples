import React from 'react'
import { Link } from 'react-router-dom'


const ProjectItem = ({project, deleteProject}) => {
    return (
        <tr>
            <td>
                {project.name}
            </td>
            <td>
                {project.user.map((user) => user.username + ' ')}
            </td>
            <td>
                {project.link_to_repo}
            </td>
            <td>
                <button onClick={()=>deleteProject(project.url)} type='button'>Delete</button>
            </td>
        </tr>
    )
}


const ProjectList = ({projects, deleteProject, searchProject}) => {
    return (
        <div>
        <label for="search">Search project by name </label>
        <input type="text" id="search"/>
        <button onClick={()=>searchProject(document.getElementById('search').value)} type='button'>Search</button>
        <table>
            <th>
                Project Name
            </th>
            <th>
                Users
            </th>
            <th>
                Link to repository
            </th>
            <th></th>
            {projects.map((project) => <ProjectItem project={project} deleteProject={deleteProject}/>)}
        </table>
        <Link to='/projects/create'>Create</Link>
        </div>
    )
}


export default ProjectList