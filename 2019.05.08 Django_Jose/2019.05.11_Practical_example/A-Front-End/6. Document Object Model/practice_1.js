var header=document.querySelector("h1")

function change_color(){
  var letters="0123456789ABCDEF";
  var color ="#"
  for (var i =0; i < 6; i++) {
    color += letters[Math.floor(Math.random()*16)]
    }

  header.style.color = color;
}
setInterval("change_color()",5);
