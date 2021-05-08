var colour = $(".selected").css("background-color");
var canvas = document.getElementById("mainCanvas");
var context = canvas.getContext("2d");
var lastEvent;
var mouseDown = false;

// When clicking on colours items
$(".controls").on("click", "li", function () {

    if ($(this).css("background-color") !== "rgba(0, 0, 0, 0)"){
            $(this).siblings().removeClass("selected");
            $(this).addClass("selected");
            colour = $(this).css("background-color");
    }
});

// On mouse events on the canvas

canvas.addEventListener("mousedown", function (e) {
    lastEvent = e;
    mouseDown = true;
}, false);

canvas.addEventListener("mousemove", function (e) {
    // Draw lines
    if (mouseDown) {
        context.beginPath();
        context.moveTo(lastEvent.offsetX, lastEvent.offsetY);
        context.lineTo(e.offsetX, e.offsetY);
        context.strokeStyle = colour;
        context.lineWidth = 5;
        context.lineCap = 'round';
        context.stroke();
        lastEvent = e;
    }
}, false);

canvas.addEventListener("mouseup", function (e) {
    mouseDown = false;
}, false);

canvas.addEventListener("mouseleave", function (e) {
    mouseDown = false;
}, false);

// Set up touch events for mobile, etc
canvas.addEventListener("touchstart", function (e) {
e.preventDefault();
        mousePos = getTouchPos(canvas, e);
  var touch = e.touches[0];
  var mouseEvent = new MouseEvent("mousedown", {
    clientX: touch.clientX,
    clientY: touch.clientY
  });
  canvas.dispatchEvent(mouseEvent);
  e.preventDefault();
}, false);
canvas.addEventListener("touchend", function (e) {
e.preventDefault();
  var mouseEvent = new MouseEvent("mouseup", {});
  canvas.dispatchEvent(mouseEvent);
  e.preventDefault();
}, false);
canvas.addEventListener("touchmove", function (e) {
e.preventDefault();
  var touch = e.touches[0];
  var mouseEvent = new MouseEvent("mousemove", {
    clientX: touch.clientX,
    clientY: touch.clientY
  });
  canvas.dispatchEvent(mouseEvent);
  e.preventDefault();
}, false);

// Get the position of a touch relative to the canvas
function getTouchPos(canvasDom, touchEvent) {
  var rect = canvasDom.getBoundingClientRect();
  return {
    x: touchEvent.touches[0].clientX - rect.left,
    y: touchEvent.touches[0].clientY - rect.top
  };
}

// Prevent scrolling when touching the canvas
document.body.addEventListener("touchstart", function (e) {
  if (e.target == canvas) {
    e.preventDefault();
  }
}, false);

document.body.addEventListener("touchend", function (e) {
  if (e.target == canvas) {
    e.preventDefault();
  }
}, false);

document.body.addEventListener("touchmove", function (e) {
  if (e.target == canvas) {
    e.preventDefault();
  }
}, false);

// Clear the canvas when button is clicked
function clear_canvas_width() {
    var s = document.getElementById("mainCanvas");
    var w = s.width;
    s.width = 10;
    s.width = w;
}