const accept= document.querySelector("#accept-btn");

const reject = document.querySelector("#reject-btn");

accept.addEventListener("click", function () {
    document.getElementById("status-content").innerHTML="Rejected";

});