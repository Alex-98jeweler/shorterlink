

function serializeData(long_url) {
    var json = {
        'long_url': long_url
    }
    return json
}

function get_long_url() {
    var input = document.getElementById('long_url');
    return input.value
}

function show_error() {
    var text = document.getElementById('input_error');
    text.style.display = true;
}

async function handleForm(event) {
    event.preventDefault();
    let long_url = get_long_url()
    json = serializeData(long_url);
    try {
        response = await fetch('/create_short_link/', {method: "POST", body: JSON.stringify(json), headers: {'Content-Type': 'application/json'}})
    } catch {
        show_error()
    }
    if (response.status === 200) {
        responseBody = await response.json();
        window.location.href = "result/" + responseBody.id;
    }
}

form = document.getElementById('link_form')
form.addEventListener('submit', handleForm)