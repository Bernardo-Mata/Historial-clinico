// Ocultar los "this field is required"

window.onload = function() {
    var errorMessages = document.getElementsByClassName('errorlist');
    for (var i = 0; i < errorMessages.length; i++) {
        errorMessages[i].style.display = 'none';
        
    }
}