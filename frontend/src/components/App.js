import React from 'react';
import Layout from './Layout';
import {BrowserRouter, Switch, Route} from 'react-router-dom';
import Home from '../pages/Home';
// import Projects from '../pages/Projects';


function App() {
  return (
    <BrowserRouter>
    <Layout>
      <Switch>
        <Route exact path="/" component={Home}/>
        {/* <Route exact path="/Projects/" component={Projects}/> */}
      </ Switch>
    </Layout>
    </BrowserRouter>
  );
}

export default App;