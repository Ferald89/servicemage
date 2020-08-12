import React from 'react';

import './styles/Signup.css'
import platziconfLogoImage from '../images/logod.svg';
import SignupForm from '../components/SignupForm';


class Signup extends React.Component{
    state = {
        loading: false,
        form :{
            email: '',
            password: '',
        },
        error: null,
        access_token: '',
    };

    render(){
        return(
            <React.Fragment>
                <div className="Signup">
                    <div className="container">
                        <div className="Signup__col">
                        <img
                        src={platziconfLogoImage}
                        alt="Deica Logo"
                        className="Signup_img"
                        />
                        <h1>Registro</h1>
                        <SignupForm/>
                        </div>
                    </div>
                </div>
            </React.Fragment>
        )
    }
}

export default Signup;
