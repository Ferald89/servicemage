import React from 'react';

import MachineDetails from './MachineDetails';
import PageLoading from '../components/PageLoading';
import PageError from '../components/PageError';
import api from '../api';


class MachineDetailsContainer extends React.Component {
  state = {
    loading: true,
    error: null,
    data: undefined,
  };

  componentDidMount() {
    this.fetchData();
  }

  fetchData = async () => {
    this.setState({ loading: true, error: null });
    console.log("jell");
    
    console.log(this.props.match.params.machineserial_number);
    try {
      const data = await api.badges.read(this.props.match.params.machineserial_number);
      console.log("entroo");
      console.log(data.body);
      this.setState({ loading: false, data: data.body});
    } catch (error) {
      this.setState({ loading: false, error: error });
    }
  };

  render() {
    if (this.state.loading) {
      return (
          <div>

              <PageLoading />
          </div>
        );
    }

    if (this.state.error) {
      return <PageError error={this.state.error} />;
    }

    return <MachineDetails machine={this.state.data} />;
  }
}

export default MachineDetailsContainer;