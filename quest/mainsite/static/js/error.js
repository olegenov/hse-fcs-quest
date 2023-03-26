const button = document.getElementById("CloseError");

function ErrorClose () {
    const error = document.getElementById("Error");
    error.classList.add("hide")
}

button.addEventListener('click', ErrorClose)