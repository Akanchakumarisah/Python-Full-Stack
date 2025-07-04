function showMessage() { 
    console.log("Click Me Button is pressed")
    alert("Inline event Triggered!")
}

const button = document.getElementById("my_button")
button.onclick = function (event) { 
    // alert("External event triggred!")
    console.log(`Event Type: ${event.type}`)
    console.log(`Target Element: ${event.target.tagName}`)
}