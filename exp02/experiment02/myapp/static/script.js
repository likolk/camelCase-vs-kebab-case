const questions = [
    {
        sentence: 'move south',
        identifiers: ['move-source', 'move-south', 'more-south', 'mover-sound'],
        correctAnswer: 'move-south'
    },
    {
        sentence: 'move north',
        identifiers: ['move-northern', 'move-north', 'move-nprth', 'move-borth'],
        correctAnswer: 'move-north'
    },
    // {
    //     sentence: 'move east',
    //     identifiers: ['move-east', 'move-easy', 'move-est', 'move-ast'],
    //     correctAnswer: 'move-east'
    // },
    // {
    //     sentence: 'move west',
    //     identifiers: ['move-wast', 'move-vest', 'move-uest', 'move-west'],
    //     correctAnswer: 'move-west'
    // },
    // {
    //     sentence: 'move up',
    //     identifiers: ['move-p', 'move-pp', 'move-up', 'move-uo'],
    //     correctAnswer: 'move-up'
    // },
    // {
    //     sentence: 'move down',
    //     identifiers: ['move-down', 'move-don', 'move-donw', 'move-dow'],
    //     correctAnswer: 'move-down'
    // },

]



// get question index
const getQuestionIndex = (question) => {
    return questions.indexOf(question)
}

let shownQuestions = []


const questionContainer = document.getElementById('questionContainer');

let randomQuestionIndex = Math.floor(Math.random() * questions.length)


function displayFirstQuestion() {
    const selectedQuestion = questions[randomQuestionIndex];
    shownQuestions.push(selectedQuestion)
    const { sentence, identifiers } = selectedQuestion;

    const optionsHTML = identifiers.map(identifier => `
        <button class="option" value="${identifier}">${identifier}</button>
    `).join('');

    const questionFormHTML = `
        <h2>Pick the correct sentence that matches: ${sentence}</h2>
        <div class="options-container">${optionsHTML}</div>
    `;

    console.log("Displaying first question:", selectedQuestion);
    console.log("Generated HTML:", questionFormHTML);
    console.log("Correct answer:", selectedQuestion.correctAnswer);

    questionContainer.innerHTML = questionFormHTML;

    const optionButtons = document.querySelectorAll('.option');
    optionButtons.forEach(button => {
        button.addEventListener('click', () => {
            const selectedAnswer = button.value;
            console.log(`Selected answer: ${selectedAnswer}`);
            const isCorrect = selectedAnswer === selectedQuestion.correctAnswer;
            console.log(`Is Correct? ${isCorrect}`);
            if (isCorrect) {
                Swal.fire({
                    title: "Your answer is correct ",
                    icon: "success",
                    timer: 10000,
                    timerProgressBar: true,
                    showConfirmButton: true,
                    grow: true,
                    confirmButtonColor: 'green',
                    allowClickOutside: true,
                });
                console.log("since correct, calling next")
                nextQuestion();
                console.log("called")
            } else {
                Swal.fire({
                    title: "Your answer is not correct ",
                    icon: "error",
                    timer: 10000,
                    timerProgressBar: true,
                    showConfirmButton: true,
                    grow: true,
                    allowClickOutside: true,
                    confirmButtonColor: 'green',
                });
            }
        });
    });
    
}


function displayQuestion(index) {
    const selectedQuestion = questions[index];
    const { sentence, identifiers } = selectedQuestion;
    shownQuestions.push(selectedQuestion)
    const optionsHTML = identifiers.map(identifier => `
        <button class="option" value="${identifier}">${identifier}</button>
    `).join('');

    const questionFormHTML = `
        <h2>Pick the correct sentence that matches: ${sentence}</h2>
        <div class="options-container">${optionsHTML}</div>
    `;

    console.log("Displaying question:", selectedQuestion);
    console.log("Generated HTML:", questionFormHTML);
    console.log("Correct answer:", selectedQuestion.correctAnswer);

    questionContainer.innerHTML = questionFormHTML;

    const optionButtons = document.querySelectorAll('.option');
    optionButtons.forEach(button => {
        button.addEventListener('click', () => {
            const selectedAnswer = button.value;
            console.log(`Selected answer: ${selectedAnswer}`);
            const isCorrect = selectedAnswer === selectedQuestion.correctAnswer;
            console.log(`Is Correct? ${isCorrect}`);
            if (isCorrect) {
                Swal.fire({
                    title: "Your answer is correct ",
                    icon: "success",
                    timer: 10000,
                    timerProgressBar: true,
                    showConfirmButton: true,
                    grow: true,
                    confirmButtonColor: 'green',
                    allowClickOutside: true,
                });
                console.log("since correct, calling next")
                nextQuestion();
                console.log("called")
            } else {
                Swal.fire({
                    title: "Your answer is not correct ",
                    icon: "error",
                    timer: 10000,
                    timerProgressBar: true,
                    showConfirmButton: true,
                    grow: true,
                    allowClickOutside: true,
                    confirmButtonColor: 'green',
                });
            }
        });
    });
}

function nextQuestion() {
    console.log("next called")
    if (shownQuestions.length < questions.length) {
        let randomQuestionIndex = Math.floor(Math.random() * questions.length)
        if (shownQuestions.includes(questions[randomQuestionIndex])) {
            nextQuestion();
        } else {
            displayQuestion(randomQuestionIndex);
        }
    } else {
        Swal.fire({
            title: "Congratulations! You have succesfully completed the experiment",
            icon: "success",
            timer: 10000,
            timerProgressBar: true,
            showConfirmButton: true,
            grow: true,
            confirmButtonColor: 'green',
            allowClickOutside: true,
        });
    }
}

window.onload = () => {
    displayFirstQuestion();
}











