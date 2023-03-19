"use strict";
window.addEventListener("load", main);

function main() {

  var userInput = document.getElementById("intext");
  var submitButton = document.getElementById('subButton');
  var encButton = document.getElementById('encButton0');
  var decButton = document.getElementById('decButton0');


  var eDMenu = document.getElementById("EDMenu");

  encButton.addEventListener("click", displayEncForm);
  decButton.addEventListener("click", displayDecForm);
  submitButton.addEventListener("click", displayOptions);

  function displayEncForm() {

    window.sessionStorage.setItem("kw", userInput.value);
    window.location.href = "encrypt.html";
  }

  function displayDecForm() {
    window.sessionStorage.setItem("kw", userInput.value);
    window.location.href = "decrypt.html";
  }


  function displayOptions() {
    if ( strip(userInput.value) == "" ) {
      alert("Please input a keyword.");
    }
    else {
      eDMenu.style.visibility = "visible";
    }
  }
}
