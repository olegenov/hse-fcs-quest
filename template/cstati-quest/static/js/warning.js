const warningButton = document.getElementById("WarningButton");

function WarningClose () {
    const warning = document.getElementById("Warning");
    warning.classList.add("hide")
}

warningButton.addEventListener('click', WarningClose)