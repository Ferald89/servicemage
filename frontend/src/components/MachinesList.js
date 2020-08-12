import React from 'react';
import { Link } from 'react-router-dom';

import './styles/MachinesList.css';
// import Gravatar from './Gravatar';

class MAchinesListItem extends React.Component {
  render() {
    return (
      <div className="MachinesListItem">

        <img src="" alt="imagen"/>

        <div>
          <strong>
            Nombre De Máquina: {this.props.machine.name}<br />
            Número De Serie: {this.props.machine.serial_number}
          </strong>
          <br />
          Modelo: {this.props.machine.model}
          <br />
          Acerca de :{this.props.machine.about}<br />
          Proximo Servicio :{this.props.machine.next_service}
        </div>
       </div>
    );
  }
}

class MachinesList extends React.Component {
  render() {
    if (this.props.machines.length === 0) {
      console.log(this.props.machines.length);
      return (
        <div>
          <h3>No badges were found</h3>
          <Link className="btn btn-primary" to="/machines/new">
            Create new badge
          </Link>
        </div>
      );
    }

    return (
      <div className="MachinesList">
        <ul className="list-unstyled">
          {this.props.machines.map(machine => {
            return (
              <li key={machine.serial_number}>
                <Link
                  className="text-reset text-decoration-none"
                  to={`/machines/${machine.serial_number}`}
                >
                  <MAchinesListItem machine={machine} />
                </Link>
              </li>
            );
          })}
        </ul>
      </div>
    );
  }
}

export default MachinesList;