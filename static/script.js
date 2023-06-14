function playSound() {
    const sound = document.getElementById("sound");
    sound.play();
  }


document.querySelector("button").addEventListener("click", function() {
    playSound()
    document.querySelector("#count").innerHTML = parseInt(document.querySelector("#count").innerHTML) + 1
    fetch('/add', {
      method: 'POST',})

  });