import React from 'react'
import {useParams} from 'react-router-dom'


const ProjectItem = ({project}) => {
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
        </tr>
    )
}


const UserProjectList = ({projects}) => {
    let {username} = useParams()
    let filtered_projects = projects.filter((project) => project.user.map((user) => user.username).includes(username))
    return (
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
            {filtered_projects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}


export default UserProjectList