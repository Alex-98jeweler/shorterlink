


function validate_custom_name(event) {
    var customNameField = document.getElementById("custom_name");
    var value = customNameField.value;
    result = value.match('^[a-z](-?[a-z])*$')
    var error = document.getElementById('input_error_custom_name')
    if (!result) {
        error.style.display = 'block';
    } else {
        error.style.display = 'none';
    }
    if (event.keyCode === 8 && error) {
        error.style.display = 'none';
    }
}

customName = document.getElementById("custom_name");
customName.addEventListener('keyup', validate_custom_name);