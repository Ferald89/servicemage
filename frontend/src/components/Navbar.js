import React from 'react';
import { Link } from 'react-router-dom';
import logo from '../images/logod.svg'
import './styles/Navbar.css'

class Navbar extends React.Component{
    render(){
        return(
            <div className="Navbar" >
                <div className="container-fluid">
                    <Link to="">
                        <img className="Navbar__brand-logo" src={logo} alt="Logo"/>
                        <span className="font-weight-light">Deica</span>
                        <span className="font-weight-bold">ServiceManagment</span>
                    </Link>
                </div>
            </div>);
        }
    };


export default Navbar;
