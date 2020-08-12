import React from 'react';
import Layout from './Layout';
import {BrowserRouter, Switch, Route} from 'react-router-dom';
import Home from '../pages/Home';
// import Projects from '../pages/Projects';
import Signup from '../pages/Signup';


function App() {
  return (
    <BrowserRouter>
    <Layout>
      <Switch>
        <Route exact path="/" component={Home}/>
        <Route exact path="/Signup" component={Signup}/>
        {/* <Route exact path="/Projects/" component={Projects}/> */}
      </ Switch>
    </Layout>
    </BrowserRouter>
  );
}

export default App;