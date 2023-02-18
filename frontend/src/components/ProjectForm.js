import React from 'react'


class ProjectForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {name: '', user: props.users[0]?.email, link_to_repo: ''}
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
        this.props.createProject(this.state.name, this.state.user, this.state.link_to_repo)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
                <div className="form-group">
                <label for="name">name</label>
                    <input type="text" className="form-control" name="name"
                        value={this.state.name} onChange={(event)=>this.handleChange(event)} />
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
                <label for="link_to_repo">link_to_repo</label>
                    <input type="string" className="form-control" name="link_to_repo"
                        value={this.state.link_to_repo} onChange={(event)=>this.handleChange(event)} />
                </div>
                <input type="submit" className="btn btn-primary" value="Save" />
            </form>
        );
    }
}


export default ProjectForm