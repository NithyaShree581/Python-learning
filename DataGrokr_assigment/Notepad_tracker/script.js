const editor = document.getElementById("editor");

const filePathInput = document.getElementById("file-path");

let typingTimer;


editor.addEventListener("input", function () {

    clearTimeout(typingTimer);

    typingTimer = setTimeout(function () {

        fetch("/save", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                file_path: filePathInput.value,
                content: editor.value
            })
        })

        .then(response => response.json())

        .then(data => {
            console.log(data.message);
        });

    }, 1000);

});