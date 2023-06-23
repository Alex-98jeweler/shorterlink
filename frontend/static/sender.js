

function serializeData(long_url, custom_name) {
    var json = {
        'long_url': long_url,
        'custom_name': custom_name
    }
    return json
}

function get_long_url() {
    var input = document.getElementById('long_url');
    return input.value
}

function get_custom_name() {
    var input = document.getElementById('custom_name');
    if (input.value === "") {
        return null
    }
    return input.value
}

function show_error() {
    var text = document.getElementById('input_error');
    text.style.display = 'block';
}

async function handleForm(event) {
    event.preventDefault();
    let long_url = get_long_url()
    let custom_name = get_custom_name()
    json = serializeData(long_url, custom_name);
    await fetch('/create_short_link/', 
                            {
                                method: "POST", 
                                body: JSON.stringify(json), 
                                headers: {'Content-Type': 'application/json'}
                            }
                            ).then((resp) => {
                                    if (resp.ok) {
                                        json = resp.json();
                                        return json
                                    }
                                    throw new Error('Siska piska')
                                } 

                                ).then((json) => {
                                    window.location.href = "result/" + json.id;
                                }
                                )
                                .catch((error) => {
                                    console.log('Piska siska');
                                    show_error();
                                }
                                
                                )
}

form = document.getElementById('link_form')
form.addEventListener('submit', handleForm)