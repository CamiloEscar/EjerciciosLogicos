let matriz = [
  ["1", "2", "3"],
  ["4", "5", "6"],
  ["7", "8", ""],
];

let board = document.querySelector(".board"); //se crea una variable obtenida de la clase board

drawTokens();
addEventListeners();

function drawTokens() {
  matriz.forEach((row) =>
    row.forEach((element) => {
      //itera por cada elemento de cada elemento
      if (element == "") {
        board.innerHTML += `<div class='empty'> ${element}</div>`; //elemento vacio
      } else {
        board.innerHTML += `<div class='token'> ${element}</div>`; //todos los elementos
      }
    })
  );
}

function addEventListeners() {
  let tokens = document.querySelectorAll(".token"); //obtiene todos los elementos token
  tokens.forEach((token) =>
    token.addEventListeners("click", () => {
      //escucha cada click
      let actualPosition = searchPosition(token.innerText);
    })
  );
}

function searchPosition(element) {
  matriz.forEach((row, index) => {
    let rowElement = row.findIndex((item) => item == element);
  });
}
// https://www.youtube.com/watch?v=Oiicrg75Y5o