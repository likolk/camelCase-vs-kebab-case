const questions = [
    {
        sentence: 'i have no idea',
        identifiers: ['iHaveN0Idea', '1HaveNoIdea', 'iHaveNoIdea', 'iHaveIdea'],
        correctAnswer: 'iHaveNoIdea'
    },
    {
        sentence: 'i am a student',
        identifiers: ['i-am-a-student', 'i-am-an-student', 'i-am-a-studend', 'i-am-a-studend'],
        correctAnswer: 'i-am-a-student'
    },
    {
        sentence: "experimentation and evaluation course",
        identifiers: ['experimentation-and-evaluation-curse','experimentation-and-evaluation-course', 'experimentation-and-evaluation-coarse', 'experinentation-and-evaluation-course'],
        correctAnswer: 'experimentation-and-evaluation-course'
    },
    {
        sentence: "eat lunch at mensa",
        identifiers: ['eat-lunch-at-mensa', 'eat-lanch-at-mensa', 'eat-launch-at-mensa', 'it-lunch-at-mensa'],
        correctAnswer: 'eat-lunch-at-mensa'
    },
    {
        sentence: "Università della Svizzera italiana",
        identifiers: ['universitàDellaSvizzerataliana', 'universitàDellaSvizzeraItaliano', 'universitàDellaSvizzeraItaliana', 'universitàDellaSvizzeraItaliama'],
        correctAnswer: 'universitàDellaSvizzeraItaliana'
    },
    {
        sentence: "180 ECTS",
        identifiers: ['18O-ECTS', '180-ECTS', '180-ETCS', '780-ECTS'],
        correctAnswer: '180-ECTS'
    },
    {
        sentence: "I am a university student",
        identifiers: ['iAmAnUniversityStudent', 'iAmAUniversityStudent', 'AmAUniversityStudent', 'iAmUniversityStudent'],
        correctAnswer: 'iAmAUniversityStudent'
    },
    {
        sentence: "tomorrow it is gonna be rainy",
        identifiers: ['tomorrowItIsGonnaBeRany', 'tomorrowItIsGonneBeRainy', 'tomorrowItIsGonnaBeRaney', 'tomorrowItIsGonnaBeRainy'],
        correctAnswer: 'tomorrowItIsGonnaBeRainy'
    }, 
    {
        sentence: "Looking forward to the Christmas Holidays",
        identifiers: ['lokingForwardToTheChristmasHolidays', 'lookingForwardToTheChristmasHoliday', 'lookingForwardToTheChristmasHolidays', 'lookingForwardToTheChristmasHollidays'],
        correctAnswer: 'lookingForwardToTheChristmasHolidays'  
    },
    {
        sentence: "This is a sentence",
        identifiers: ['this-a-sentence', 'this-is-a-sentence', 'this-is-a-sentences', 'these-a-is-sentence'],
        correctAnswer: 'this-is-a-sentence'
    }
]



let startTime;
let totalTimeTaken = 0;
let interval;

// get question index


let shownQuestions = []

let timeTakenToAnswerEachQuestion = []


const questionContainer = document.getElementById('questionContainer');

let randomQuestionIndex = Math.floor(Math.random() * questions.length)


function displayFirstQuestion() {
    const urlParams = new URLSearchParams(window.location.search);
    const session_id = urlParams.get('session_id');
    console.log("session_id", session_id)


    startTime = new Date()
    const selectedQuestion = questions[randomQuestionIndex];
    shownQuestions.push(selectedQuestion)
    const { sentence, identifiers } = selectedQuestion;

    const shuffled_identifiers = shuffle_responses(identifiers);

    const optionsHTML = shuffled_identifiers.map(identifier => `
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
            const endTime = new Date();
            const timeTaken = (endTime - startTime) / 1000;
            totalTimeTaken += timeTaken;
            timeTakenToAnswerEachQuestion.push(timeTaken);
            console.log("Time taken for question 1:", timeTaken);
            console.log("TOTAL TIME TAKEN UNTIL NOW:", totalTimeTaken)
            console.log("saving response")
            sendResponseToServer(session_id, selectedQuestion.sentence, selectedAnswer, timeTaken, isCorrect);
            console.log("response should be saved")
            if (isCorrect) {
                Swal.fire({
                    title: "Your answer is correct ",
                    text: `You took ${timeTaken} seconds to answer correctly this question`,
                    icon: "success",
                    timer: 10000,
                    timerProgressBar: true,
                    showConfirmButton: true,
                    grow: true,
                    confirmButtonColor: 'green',
                    allowClickOutside: true,
                }).then(() => {
                    startTimer()
                    nextQuestion();
                })
                timeTaken = 0;
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
                }).then(() => {
                    startTimer()
                    nextQuestion();
                })
                timeTaken = 0;
            }
        });
    });
}


function displayQuestion(index) {
    const urlParams = new URLSearchParams(window.location.search);
    const session_id = urlParams.get('session_id');
    console.log("session_id", session_id)
    startTime = new Date()
    const selectedQuestion = questions[index];
    const { sentence, identifiers } = selectedQuestion;
    shownQuestions.push(selectedQuestion)
    const shuffled_identifiers = shuffle_responses(identifiers);
    const optionsHTML = shuffled_identifiers.map(identifier => `
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
            const endTime = new Date();
            const timeTaken = (endTime - startTime) / 1000;
            totalTimeTaken += timeTaken;
            timeTakenToAnswerEachQuestion.push(timeTaken);
            console.log(`Time taken for question ${selectedAnswer}`, timeTaken);
            console.log("TOTAL TIME TAKEN UNTIL NOW:", totalTimeTaken)
            console.log("saving response")
            sendResponseToServer(session_id, selectedQuestion.sentence, selectedAnswer, timeTaken, isCorrect);
            console.log("response should be saved")
            if (isCorrect) {
                Swal.fire({
                    title: "Your answer is correct ",
                    text: `You took ${timeTaken} seconds to answer correctly this question`,
                    icon: "success",
                    timer: 10000,
                    timerProgressBar: true,
                    showConfirmButton: true,
                    grow: true,
                    confirmButtonColor: 'green',
                    allowClickOutside: true,
                }).then(() => {
                    startTimer()
                    nextQuestion();
                })
                timeTaken = 0;
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
                }).then(() => {
                    startTimer()
                    nextQuestion();
                })
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
        totalTimeTaken = totalTimeTaken.toFixed(2);
        Swal.fire({
            title: "Congratulations! You have succesfully completed the experiment",
            text: `You took ${totalTimeTaken} seconds to answer all questions`,
            icon: "success",
            timer: 10000,
            timerProgressBar: true,
            showConfirmButton: true,
            grow: true,
            confirmButtonColor: 'green',
            allowClickOutside: true,
            confirmButtonText: "Go to Home Page",
        }).then(() => {
            console.log("calling compile")
            compilePostgresql()
            window.location.href = "/"   
        })
    }
}
 
function compilePostgresql() {
    console.log("called compile")
    fetch('/compile-postgresqlToCSV/', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log("data", data)
    })
    .catch(error => {
        console.error('Error compiling PostgreSQL:', error);
    });
    console.log("Finito");
}


function startTimer() {
    startTime = new Date();
    interval = setInterval(() => {
        const currentTime = new Date();
        const timeElapsed = (currentTime - startTime) / 1000;
        console.log("Time elapsed:", timeElapsed);
    }, 1000);
}
// function to get the CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        console.log("document.cookie", document.cookie)
        const cookies = document.cookie.split(';');
        console.log("cookies", cookies)
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            console.log("cookie", cookie)
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === name + '=') {
                console.log("cookie.substring(0, name.length + 1)", cookie.substring(0, name.length + 1))
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                console.log("cookieValue", cookieValue)
                break;
            }
        }
    }
    return cookieValue;
}

window.onload = () => {
    displayFirstQuestion();
}




function sendResponseToServer(session_id, question, answer, timeTaken, isCorrect) {
    // get the session id generated in the python file

    fetch('/save-response/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({
            session_id:  session_id,
            question: question,
            answer: answer,
            time_taken: timeTaken,
            is_correct: isCorrect
        })
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        }
        throw new Error('Network response was not ok.');
    })
    .then(data => {
        console.log('Response saved successfully:', data);
    })
    .catch(error => {
        console.error('Error saving response:', error);
    });
}


function shuffle_responses(responses) {
    let currentIndex = responses.length;
    let randomIndex;
    // while there are still elements to shuffle
    while (currentIndex > 0) {
        randomIndex = Math.floor(Math.random() * currentIndex)
        currentIndex -= 1;
        // swap it with the current element
        [responses[currentIndex], responses[randomIndex]] = [responses[randomIndex], responses[currentIndex]]
    }
    return responses;
}


