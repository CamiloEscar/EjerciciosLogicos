const quizData = [
    {
        question: "Cual lenguaje corre en una pagina web?",
        a: "Java",
        b:"C",
        c: "Python",
        d: "JavaScript",
        correct: "d",
    },
    {
        question: "Que significa CSS?",
        a:"Central Style Sheets",
        b:"Cascading Style Sheets",
        c:"Cascading Simple Sheets",
        d:"Cars SUVs Sailboats",
        correct:"b",
    },
    {
        question: "Que significa HTML?",
        a:"Hypertext Markup Language",
        b:"Hypertext Markdown Language",
        c:"Hyperloop Machine Language",
        d:"Helicopters Terminals Motorboats Lamborginis",
        correct:"a",
    },
    {
        question: "En que año fue lanzado JavasCript?",
        a:"1996",
        b:"1995",
        c:"1994",
        d:"ninguna de las anteriores",
        correct:"b",
    }
];

const quiz = document.getElementById('quiz')
const answerEls = document.querySelectorAll('.answer')
const questionEl = document.getElementById('question')
const a_text = document.getElementById('a_text')
const b_text = document.getElementById('b_text')
const c_text = document.getElementById('c_text')
const d_text = document.getElementById('d_text')
const submitBn = document.getElementById('submit')

let currentQuiz = 0
let score = 0

loadQuiz()

function loadQuiz () {
    deselectAnswers()

    const currentQuizData = quizData[currentQuiz]

    questionEl.innerText = currentQuizData.question
    a_text.innerText = currentQuizData.a
    b_text.innerText = currentQuizData.b
    c_text.innerText = currentQuizData.c
    d_text.innerText = currentQuizData.d
}

function deselectAnswers() {
    answerEls.forEach(answerEl => answerEl.checked = false)
}

function getSelected() {
    let answer

    answerEls.forEach(answerEl => {
        if(answerEl.checked) {
            answer = answerEl.id
        }
    })
    return answer
}

submitBn.addEventListener('click', () => {
    const answer = getSelected()

    if(answer) {
        if(answer === quizData[currentQuiz].correct) {
            score++
        }

        currentQuiz++

        if(currentQuiz < quizData.length) {
            loadQuiz()
        } else {
            let resultText = `<h2>Respondiste ${score}/${quizData.length} preguntas correctas</h2>`;
            
            if (score === quizData.length) {
                resultText += "😎"; 
            } else if (score >= quizData.length / 2) {
                resultText += "😒";
            } else {
                resultText += "😢";
            }

            resultText += `<button onclick="location.reload()">Recargar</button>`;
            quiz.innerHTML = resultText;
        }
    }
})
