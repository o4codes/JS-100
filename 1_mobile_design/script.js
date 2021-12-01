let names = ["Shadrach","Jerome","Chiazam"]

for (const elem of names) {
    console.error(elem)
}

// setup listener
document.addEventListener("DOMContentLoaded", function() {
    let button = document.getElementById("button")
    button.addEventListener("click", function() {
        console.log("button clicked")
    })
})

//get element by id
let button = document.getElementById("button")

// iterate over object
let obj = {
    name: "Shadrach",
    age: 25,

    // method
    sayHello: function() {
        console.log("Hello")
    }
}
