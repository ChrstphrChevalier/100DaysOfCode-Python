const editor = document.getElementById("editor");
let timeout = null;

function resetTimer() {
  if (timeout) clearTimeout(timeout);
  timeout = setTimeout(() => {
    editor.value = "";
    alert("Temps écoulé ! Votre texte a été supprimé.");
  }, 5000); // 5 secondes
}

editor.addEventListener("input", resetTimer);
