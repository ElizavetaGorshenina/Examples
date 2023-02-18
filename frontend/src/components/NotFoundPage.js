import React from 'react'


const NotFound404 = ({ location }) => {
    return (
      <div>
        <h1>Page `{location.pathname}` not found</h1>
      </div>
    )
  }


  export default NotFound404