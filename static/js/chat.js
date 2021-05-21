const form = document.querySelector(".typing-area"),
    inputField = form.querySelector(".input-field"),
    sendBtn = form.querySelector("button"),
    chatBox = document.querySelector(".chat-box");

inputField.focus();
var userRawText = form.querySelector("textInput").val();

function alertSend() {
    alert(inputField);
}
function scrollToBottom() {
    chatBox.scrollTop = chatBox.scrollHeight;
}