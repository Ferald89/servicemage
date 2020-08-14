import React from 'react';
// import ReactDOM from 'react-dom';
// import { Link } from 'react-router-dom';

// import './styles/BadgeDetails.css';
// import confLogo from '../images/platziconf-logo.svg';
import Machine from '../components/machine';

function MachineDetails(props) {
  const machine = props.machine;
  console.log(machine);
  console.log(machine.user[0].email);

  return (
    <div>
      <div className="BadgeDetails__hero">
        <div className="container">
          <div className="row">
            <div className="col-6">
              {/* <img src={confLogo} alt="Logo de la Conferencia" /> */}
                <h1>{machine.machine.name}</h1>
            </div>
            <div className="col-6 BadgeDetails__hero-attendant-name">
              <h1>
                {machine.machine.model}  <br/>
                 {machine.machine.serial_number}
              </h1>
            </div>
          </div>
        </div>
      </div>

      <div className="container">
        <div className="row">
          <div className="col">
            <Machine
              name={machine.machine.name}
              model={machine.machine.model}
              about={machine.machine.about}
              next_service={machine.machine.next_service}
              serial_number={machine.machine.serial_number}
              email={machine.user[0].email}
              name_user={machine.user[0].first_name}
            />
          </div>
          <div className="col">
            <h2>Actions</h2>
            <div>

              {/* <div>
                <button className="btn btn-danger">Delete</button>
                {ReactDOM.createPortal(
                  <h1>Hola, realmente no estoy aquí</h1>,
                  document.getElementById('modal')
                )}
              </div> */}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default MachineDetails;