function colorchange(change_object){
  letters="0123456789ABCDEf"
  color="#"
  for (var i = 0; i < 6; i++){
    color += letters[Math.floor(Math.random()*16)];
    }
  change_object.style.color = color;
}

var one = document.querySelector("#one")
var two = document.querySelector("#two")
var three = document.querySelector("#three")

one.addEventListener('mouseover',function(){
  letters="0123456789ABCDEf"
  color="#"
  for (var i = 0; i < 6; i++){
    color += letters[Math.floor(Math.random()*16)];
    }
  one.style.color = color;
}
)
two.addEventListener("click",function(){
  letters="0123456789ABCDEf"
  color="#"
  for (var i = 0; i < 6; i++){
    color += letters[Math.floor(Math.random()*16)];
    }
  two.style.color = color;
}
)
three.addEventListener("dblclick",function(){
  letters="0123456789ABCDEf"
  color="#"
  for (var i = 0; i < 6; i++){
    color += letters[Math.floor(Math.random()*16)];
    }
  three.style.color = color;
}
)
