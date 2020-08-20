import React from 'react';
import Layout from './Layout';
import {BrowserRouter, Switch, Route} from 'react-router-dom';
import Home from '../pages/Home';
import Feed from '../pages/Feed';
import MachineNew from '../pages/MachineNew';
import Signup from '../pages/Signup';
import MachineDetails from '../pages/MachineDetailsContainer';

function App() {
  return (
    <BrowserRouter>
    <Layout>
      <Switch>
        <Route exact path="/" component={Home}/>
        <Route exact path="/Signup" component={Signup}/>
        <Route exact path="/Feed" component={Feed}/>
        <Route exact path="/feed/machines/new" component={MachineNew}/>
        <Route exact path="/feed/machines/:machineserial_number" component={MachineDetails}/>
      </ Switch>
    </Layout>
    </BrowserRouter>
  );
}

export default App;