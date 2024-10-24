//almacenamos el game status
const statusDisplay = document.querySelector('.game--status')

let gameActive = true
let currentPlayer = "X"
let gameState = ["", "", "", "", "", "", "", "", ""]

//mensajes
const winningMessage = () => `Jugador ${currentPlayer} ha ganao!`
const drawMessage = () => 'Empate'
const currentPlayerTurn = () => `Turno de ${currentPlayer}`

// Inicializamos el estado del display con el turno del jugador actual
statusDisplay.innerHTML = currentPlayerTurn()

function handleCellPlayed (clickedCell, clickedCellIndex) {
    //actualizamos el estado interno del juego q es reflejado en la jugada del jugador
    gameState[clickedCellIndex] = currentPlayer;
    clickedCell.innerHTML = currentPlayer;
}

function handlePlayerChanged () {
    currentPlayer = currentPlayer === "X" ? "O" : "X"
    statusDisplay.innerHTML = currentPlayerTurn()
}

function handleResultValidation() {
    const winningConditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ];
    let roundWon = false
    for (let i = 0; i < winningConditions.length; i++) {
        const winCondition = winningConditions[i]
        let a = gameState[winCondition[0]]
        let b = gameState[winCondition[1]]
        let c = gameState[winCondition[2]]
        if (a === '' || b === '' || c === '') {
            continue
        }
        if (a === b && b === c) {
            roundWon = true
            break
        }
    }
        if (roundWon) {
            statusDisplay.innerHTML = winningMessage()
            gameActive = false
            return
        }

        let roundDraw = !gameState.includes("")
        if (roundDraw) {
            statusDisplay.innerHTML = drawMessage()
            gameActive  = false
            return
        }
        handlePlayerChanged()
}


function handleCellClick (clickedCellEvent) {
   //guardamos el elemento html de click en una variable
    const clickedCell = clickedCellEvent.target 
    
    //Aquí tomaremos el atributo 'índice de celda de datos' de la celda en la que se hizo clic para identificar dónde está esa celda en nuestra cuadrícula. Tenga en cuenta que getAttribute devolverá un valor de cadena. Como necesitamos un número real, lo analizaremos como un número integer (número) 
    const clickedCellIndex = parseInt(
        clickedCell.getAttribute('data-cell-index')
    )

    //A continuación debemos verificar si la llamada ya se jugó o si el juego está en pausa. Si cualquiera de las dos cosas es cierta, simplemente ignoraremos el clic. 
    if (gameState[clickedCellIndex] !== "" || !gameActive) {
        return
    }

    //si todo va en orden debemos proceder con el juego
    handleCellPlayed(clickedCell, clickedCellIndex)
    handleResultValidation()
}

function handleRestartGame () {
    gameActive = true
    currentPlayer = "X"
    gameState = ["", "", "", "", "", "", "", "", ""]
    statusDisplay.innerHTML = currentPlayerTurn()
    document.querySelectorAll('.cell').forEach(cell => cell.innerHTML = "")
}

document.querySelectorAll('.cell').forEach(cell =>
    cell.addEventListener('click', handleCellClick))
document.querySelector('.game--restart').addEventListener('click', handleRestartGame)