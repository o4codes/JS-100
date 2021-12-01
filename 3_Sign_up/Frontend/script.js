let name_element = document.getElementById("name");
let email_element = document.getElementById("email");
let mobile_element = document.getElementById("mobile_number");
let password_element = document.getElementById("password");
let confirm_password_element = document.getElementById("confirm_password");
let sign_up_btn = document.getElementById("sign_up_btn");

sign_up_btn.addEventListener("click", function(event) {
    event.preventDefault();

    let myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    
    let raw = JSON.stringify({
      "name": name_element.value,
      "email": email_element.value,
      "mobile": mobile_element.value,
      "password": password_element.value,
      "confirm_password": confirm_password_element.value
    });
    
    var requestOptions = {
      method: 'POST',
      headers: myHeaders,
      body: raw,
      redirect: 'follow'
    };
    
    fetch("http://127.0.0.1:8000/api/v1/users", requestOptions)
      .then(response => response.text())
      .then(result => alert("User created successfully "+result))
      .catch(error => alert("Failure "+error));

});
