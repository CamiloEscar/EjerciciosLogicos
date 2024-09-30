const resetBtn = document.querySelector('#reset')
const playBtn = document.querySelector('#play')
const timerEl = document.querySelector('#timer')
const root = document.querySelector(':root')

//inicio setup

const totalSeconds = 60
let playing = false
let currentSeconds = totalSeconds
timerEl.innerText = formatTime(totalSeconds)

const timerInterval = setInterval(run, 1000)

playBtn.addEventListener('click', () => {
    playing = !playing
    playBtn.classList.toggle('play')
    playBtn.classList.toggle('bg-green-500') //color de la clase toggle
    
    const playIcon = playBtn.querySelector('i')
    playIcon.classList.toggle('fa-play') // icono de play en verde
    playIcon.classList.toggle('fa-pause') // icono de pausa en verde
})

resetBtn.addEventListener('click', resetAll)

//inicio del temporizador
function run() {
    if (playing) {
        currentSeconds -= 1
        if(currentSeconds <= 0) {
            clearInterval(timerInterval)
            resetAll()
        }

        timerEl.innerText = formatTime(currentSeconds)
        root.style.setProperty('--degrees', calcDeg())
    }
}


//formato del tiempo
function formatTime(seconds) {
    const minutes = Math.floor(seconds / 60)
    const newSeconds = seconds % 60

    return `${minutes.toString().padStart(2, '0')}:${newSeconds
        .toString()
        .padStart(2, '0')}`
}

//calculo de los grados

function calcDeg() {
    return `${360 - (currentSeconds / totalSeconds) * 360}deg`
}

//reset de los valores

function resetAll() {
    playing = false
    playBtn.classList.remove('play')
    playBtn.classList.remove('bg-green-500') //remueve el color verde
    const playIcon = playBtn.querySelector('i')
    playIcon.classList.remove('fa-pause') //remueve el icono de pausa
    playIcon.classList.add('fa-play') //agrega el icono de play
    currentSeconds = totalSeconds
    timerEl.innerText = formatTime(totalSeconds)
    root.style.setProperty('--degrees', '0deg')
}