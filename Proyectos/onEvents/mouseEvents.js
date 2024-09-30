//onclick
button.addEventiListener("click", function () {
  alert("button was clicked!");
});

//mousedown
button.addEventiListener("mousedown", function () {
  alert("mouse button pressed down");
});

//mouseup
button.addEventiListener("mouseup", function () {
  alert("mouse button released");
});

//mousemove
button.addEventiListener("mousemove", function (e) {
  alert("mouse moved");
  //e.clientX and e.clientY are the coordinates of the mouse position
  alert("mouse position: " + e.clientX + ", " + e.clientY);
});

//mouseover
button.addEventiListener("mouseover", function () {
  alert("mouse is over the button");
});

//mouseout
button.addEventiListener("mouseout", function () {
    alert("mouse is out of the button");
    });

//mouseenter
button.addEventiListener("mouseenter", function () {
    alert("mouse entered the button");
    });

//mouseleave
button.addEventiListener("mouseleave", function () {
    alert("mouse left the button");
    });