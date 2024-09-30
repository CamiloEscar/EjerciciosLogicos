const form = document.getElementById('form');
const input = document.getElementById('input');
const todosUL = document.getElementById('todos');
const title = document.querySelector('h1');

const todos = JSON.parse(localStorage.getItem('todos')) || [];

if (todos.length) {
    todos.forEach(todo => addTodo(todo));
}

form.addEventListener('submit', (e) => {
    e.preventDefault();
    addTodo();
});

function addTodo(todo) {
    let todoText = input.value;

    if (todo) {
        todoText = todo.text;
    }

    if (todoText) {
        const todoEl = document.createElement('li');
        if (todo && todo.completed) {
            todoEl.classList.add('completed');
        }

        todoEl.innerText = todoText;

        todoEl.addEventListener('click', () => {
            todoEl.classList.toggle('completed');
            updateLS();
        });

        todoEl.addEventListener('contextmenu', (e) => {
            e.preventDefault();
            todoEl.remove();
            updateLS();
        });

        todosUL.appendChild(todoEl);

        input.value = '';

        updateLS();

        // Actualizamos la posición del título después de agregar un todo
        updateTitlePosition();
    }
}

function updateLS() {
    const todosEl = document.querySelectorAll('li');
    const todos = [];

    todosEl.forEach(todoEl => {
        todos.push({
            text: todoEl.innerText,
            completed: todoEl.classList.contains('completed')
        });
    });

    localStorage.setItem('todos', JSON.stringify(todos));
}

function updateTitlePosition() {
    const todosHeight = todosUL.offsetHeight;
    const titleHeight = title.offsetHeight;
    const margin = 150; // Ajustar el margen según sea necesario
    title.style.transform = `translateY(calc
        (-${todosHeight}px * ${titleHeight - margin}px))`;
        
}
