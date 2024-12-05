document.querySelector('.user-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const formData = new FormData(document.querySelector('.user-form'));
    const user = {};
    for (let pair of formData.entries()) {
        user[pair[0]] = pair[1];
        console.log(`${pair[0]}: ${pair[1]}`);
    }
    addUserInTable(user);
    console.log(e);
});

function addUserInTable(user) {
    const tbody = document.querySelector('tbody');
    const row = tbody.insertRow();
    const cell0 = row.insertCell(0);
    const cell1 = row.insertCell(1);
    const cell2 = row.insertCell(2);
    cell0.innerHTML = user.name;
    cell1.innerHTML = user.email;
    const buttonRemove = document.createElement('button');
    buttonRemove.className = "user-remove";
    buttonRemove.innerHTML = "Remover";
    buttonRemove.onclick = removeUserInTable;
    cell2.appendChild(buttonRemove);
}

function removeUserInTable(e) {
    e.target.parentElement.parentElement.remove();
}