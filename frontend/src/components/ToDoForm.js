import React from 'react'


class ToDoForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {text: '', user: props.users[0]?.email, project: props.projects[0]?.link_to_repo}
    }

    handleChange(event)
    {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }

    handleSubmit(event) {
        this.props.createToDo(this.state.text, this.state.user, this.state.project)
        console.log(this.state.project)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
                <div className="form-group">
                <label for="text">text</label>
                    <input type="text" className="form-control" name="text"
                        value={this.state.text} onChange={(event)=>this.handleChange(event)} />
                </div>
                <div className="form-group">
                <label for="user">user</label>
                <select name="user" className='form-control'
                    onChange={(event)=>this.handleChange(event)}>
                    {this.props.users.map((user)=><option
                    value={user.email}>{user.username}</option>)}
                </select>
                </div>
                <div className="form-group">
                <label for="project">project</label>
                <select name="project" className='form-control'
                    onChange={(event)=>this.handleChange(event)}>
                    {this.props.projects.map((project)=><option
                    value={project.link_to_repo}>{project.name}</option>)}
                </select>
                </div>
                <input type="submit" className="btn btn-primary" value="Save" />
            </form>
        );
    }
}


export default ToDoForm