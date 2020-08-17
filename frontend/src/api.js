const BASE_URL = 'https://servicemante.ga';
// const BASE_URL = 'http://localhost:8000';

const delay = ms => new Promise(resolve => setTimeout(resolve, ms));
const randomNumber = (min = 0, max = 1) =>
  Math.floor(Math.random() * (max - min + 1)) + min;
const simulateNetworkLatency = (min = 30, max = 1500) =>
  delay(randomNumber(min, max));

async function callApi(endpoint, options = {}) {
  // await simulateNetworkLatency(); 
  // console.log(localStorage.getItem("access_token"));
  // let token = "fe8901be5ba7f78a884400cce8c08e829de7f237";
  let token = localStorage.getItem("access_token");
  // console.log("este es el token " + token);
  if (token){

    options.headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Token '+token,
      Accept: 'application/json',
    };
  }
  else{
    options.headers = {
      'Content-Type': 'application/json',
      Accept: 'application/json',
    };
  }

  const url = BASE_URL + endpoint;
  const response = await fetch(url, options);
  const data = await response.json();
  // console.log(data);
  // console.log(response);
  return {status: response.ok, body: data}
}

const api = {
  badges: {
    list() {
      return callApi('/machines/');
    },
    create(badge) {
      return callApi(`/badges`, {
        method: 'POST',
        body: JSON.stringify(badge),
      });
    },
    login(badge) {
      return callApi('/users/login/', {
        method: 'POST',
        body: JSON.stringify(badge)
      });
    },
    signup(badge) {
      return callApi('/users/signup/',{
        method: 'POST',
        body: JSON.stringify(badge)
      });
    },
    read(machineserial_number) {
      return callApi(`/machines/${machineserial_number}/`);
    },
    readservice(machineserial_number) {
      return callApi(`/machines/${machineserial_number}/services/`);
    },
    update(badgeId, updates) {
      return callApi(`/badges/${badgeId}`, {
        method: 'PUT',
        body: JSON.stringify(updates),
      });
    },
    // Lo hubiera llamado `delete`, pero `delete` es un keyword en JavaScript asi que no es buena idea :P
    remove(badgeId) {
      return callApi(`/badges/${badgeId}`, {
        method: 'DELETE',
      });
    },
  },
};

export default api;