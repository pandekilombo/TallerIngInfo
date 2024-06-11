function toggleSidebar() {
    var sidebar = document.getElementById('sidebar');
    if (sidebar.style.left === '0px' || sidebar.style.left === '') {
        sidebar.style.left = '-250px';
    } else {
        sidebar.style.left = '0px';
    }
}

function logout() {
    alert('Cerrando sesión...');
    // Aquí puedes agregar la lógica para cerrar sesión, como redirigir a una página de inicio de sesión
}

function reservarEstacionamiento() {
    alert('Reservando estacionamiento...');
    // Aquí puedes agregar la lógica para reservar un estacionamiento
}

function mostrarRegistroEstacionamientos() {
    alert('Mostrando registro de estacionamientos...');
    // Aquí puedes agregar la lógica para mostrar el registro de estacionamientos
}

function mostrarSugerencias() {
    alert('Mostrando sugerencias...');
    // Aquí puedes agregar la lógica para mostrar sugerencias
}
