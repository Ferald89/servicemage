import React from 'react';


class SignupForm extends React.Component{
    render(){
        return(
            <div>
            <form>
                <div className="form-group">
                <input
                type="text"
                placeholder="email"
                />
                </div>
                <div className="form-group">
                <input
                type="text"
                placeholder="username"
                />
                </div>
                <div className="form-group">
                <input
                type="text"
                placeholder="phonenumber"
                />
                <input
                type="text"
                placeholder="password"
                />
                </div>
            </form>
            </div>
        )
    }
}

export default SignupForm;