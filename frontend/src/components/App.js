import React from 'react';
import Layout from './Layout';
import {BrowserRouter, Switch, Route} from 'react-router-dom';
import Home from '../pages/Home';
import Feed from '../pages/Feed';
import Signup from '../pages/Signup';


function App() {
  return (
    <BrowserRouter>
    <Layout>
      <Switch>
        <Route exact path="/" component={Home}/>
        <Route exact path="/Signup" component={Signup}/>
        <Route exact path="/Feed" component={Feed}/>
      </ Switch>
    </Layout>
    </BrowserRouter>
  );
}

export default App;