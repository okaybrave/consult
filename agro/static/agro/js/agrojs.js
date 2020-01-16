var mybutton = document.getElementById("myBt");

function scrollFunction() {
  if (document.body.scrollDown < 0 || document.documentElement.scrollDown < 0) {
    mybutton.style.display = "none";
  } else {
    mybutton.style.display = "none";
  }
}

function downFunction() {
  document.body.scrollTop = 550;
  document.documentElement.scrollTop = 500;
}
