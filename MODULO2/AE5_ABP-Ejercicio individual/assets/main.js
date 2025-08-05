const section_connections = document.querySelector(".sectionConections");
const number_requests = document.querySelector("#numberPendingConnections");
const container_totalConnections = document.querySelector(
  ".containerConnections"
);
const number_totalConnections = document.querySelector(
  "#numberRealConnections"
);
const name_profile = document.querySelector(".infoProfile h2");

function addConnection(event) {
  console.log("add");
  const button = event.target;
  const containerButton = button.closest(".containerRequest");
  const nameUser = containerButton.querySelector("span")?.innerHTML;
  const imgUserSrc = containerButton.querySelector("img")?.src;

  let actualNumberOfRequests = (parseInt(number_requests.textContent) || 0) - 1;
  let actualNumberTotalRequests =
    parseInt(number_totalConnections.innerHTML) + 1;

  number_requests.innerHTML = actualNumberOfRequests;
  number_totalConnections.innerHTML = actualNumberTotalRequests;
  containerButton.remove();

  const newConnection = document.createElement("div");
  newConnection.className = "containerConnection";
  newConnection.innerHTML = `<img src="${imgUserSrc}"/><span class="nameUser">${nameUser}</span>`;
  container_totalConnections.prepend(newConnection);
}

function removeConnection(event) {
  console.log("remove");
  const button = event.target;
  const containerButton = button.closest(".containerRequest");
  let actualNumberOfRequests = (parseInt(number_requests.textContent) || 0) - 1;
  number_requests.innerHTML = actualNumberOfRequests;
  containerButton.remove();
}

function editProfile() {
  name_profile.innerHTML == "Linn Olsen"
    ? (name_profile.innerHTML = "Sophia Larsen")
    : (name_profile.innerHTML = "Linn Olsen");

  // name_profile.innerHTML= new_name
}
