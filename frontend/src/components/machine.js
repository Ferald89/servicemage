import React from 'react';

import './styles/Badge.css';

// import Gravatar from './Gravatar';

class Machine extends React.Component{
    render(){
        let {model, about, next_service, serial_number, email, name_user, picture} = this.props;
        console.log("heloo "+picture);

        return <div className="Badge">


            <div className="Badge__section-name">
                <img src={picture} alt="image" className="machineimage"/>
        <h1>
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

        </div>;
    }
}

export default Machine;