const eye= document.querySelector("#eye");

const password = document.querySelector("#password");




eye.addEventListener("click", function () {

    // toggle the type attribute

    const type = password.getAttribute("type") === "password" ? "text" : "password";

    password.setAttribute("type", type);



    if(type=="password")

        eye.style.color="gray";

    else

        eye.style.color="black";

});