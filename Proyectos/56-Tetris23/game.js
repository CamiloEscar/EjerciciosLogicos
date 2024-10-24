var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");

function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  // Dibuja el juego aquí
  requestAnimationFrame(draw);

}

draw();
