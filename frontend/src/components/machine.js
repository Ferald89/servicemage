import React from 'react';

// import './styles/Badge.css';

import conflogo from '../images/badge-header.svg';
// import Gravatar from './Gravatar';

class Machine extends React.Component{
    render(){
        let {name, model, about, next_service, serial_number, email, name_user} = this.props;

        return <div className="Badge">
            <div className="Badge__header">
                {/* <img src={conflogo} alt="Logo de conferencia"/> */}
            </div>

            <div className="Badge__section-name">
                {/* <Gravatar className="Badge__avatar" email={this.props.email} /> */}
        <h1>
            {/* {name} */}
            <br/>{model}
        </h1>
            </div>

            <div className="Badge__section-info">
                <h3>{about}</h3>
                <div>{next_service}</div>
                <div>{serial_number}</div>
                <div>{email}</div>
                <div>{name_user}</div>
            </div>

            <div className="Badge__footer">
                #platziconf
            </div>
        </div>;
    }
}

export default Machine;