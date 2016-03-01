function ajax(options) {
    const DONE = 4;
    const OK = 200;

    var xhr = new XMLHttpRequest();

    xhr.open(options.method, options.url);

    xhr.onreadystatechange = function () {
        if (xhr.readyState === DONE) {
            if (xhr.status === OK) {
                options.success.call(this, xhr.responseText);
            } else {
                options.error.call(this, xhr.responseText);
            }
        }
    }

    xhr.send(null);
}