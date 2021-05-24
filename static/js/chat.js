
function buttonClick() {
    let userRawText = document.getElementById("inputMessage").value;

    let tag = document.createElement("P");
    let text = document.createTextNode(userRawText);

    tag.appendChild(text);

    document.getElementById("inputMessage").value = "";

    document.getElementById("userInput").appendChild(tag);

    // $("form").submit(function () { return false; });

}

