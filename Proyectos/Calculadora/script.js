const othersOp = document.getElementById("othersOp");
const numbers = document.getElementById("numbers");

const OTHERS_OP = [
  "X", "Calc", "", "", "Pi", "x³", "ab", 
  "√", "x²", "^", "log", "In", 
  "(-)", ".,,,", "hyp", "sin", "cos", 
  "tan", "Rc1", "Eng", "(",
  ")", ",", "m+"
]
const NUMBERS = [
  "7", "8", "9", "DEL", "AC", 
  "4", "5", "6", "*", "/", 
  "1", "2", "3", "+", "-", 
  "0", ".", "EXP", "Ans",
  "="
]

for (let index = 0; index < OTHERS_OP.length; index++) {
  const button = document.createElement("button");
  button.innerText = OTHERS_OP[index];
  othersOp.appendChild(button);
  if (index == 2 || index == 3) { button.classList.add ("hidden");}
}

for (let index = 0; index < NUMBERS.length; index++) {
  const button = document.createElement("button");
  button.innerText = NUMBERS[index];
  othersOp.appendChild(button);
  if (NUMBERS[index].includes("DEL") || NUMBERS[index].includes("AC")) {button.classList.add("color")}
}