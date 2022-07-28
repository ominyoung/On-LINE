function quizInit() {

  // Selectors
  var $quizQuestionText = $('.quiz .question .questionText');
  var $quizQuestionOptions = $('.quiz .question .options');
  var $quizProgress= $('.quiz progress');
  var $quizProgressDataCurrent= $('.quiz .progressData .current');
  var $quizProgressDataLimit= $('.quiz .progressData .limit');

  // Data input for Questions and Results
  var questions = [{
    text: '1. 어떤 여행 스타일을 좋아하세요?',
    answers: {
      type: 'multiple',
      options: [{
        text: 'A. 유명관광지 탐방여행 ',
        weight: 1
      }, {
        text: 'B. 액티비티 체험여행',
        weight: 2
      }, {
        text: 'C. 역사와 문화 여행',
        weight: 3
      },{
        text: 'D. 맛있는 먹방 여행',
        weight: 0
      }]
    },
  }, {
    text: '2.  숙박 장소로 선호 하는 곳은 어디인가요?',
    answers: {
      type: 'multiple',
      options: [{
        text: 'A. 호텔',
        weight: 0
      }, {
        text: 'B. 게스트 하우스',
        weight: 1
      }, {
        text: 'C. 캠핑장',
        weight: 2
      },{
        text: 'D. 모텔',
        weight: 3
      }]
    },
  },{
    text: '3. 여행 중 방문하고 싶은 관광지를 선태주세요',
    answers: {
      type: 'range',
      options: [{
        text: 'A. 박물관 & 미술관',
        weight: 1
      }, {
        text: 'B. 해변',
        weight: 2
      }, {
        text: 'C. 산',
        weight: 3
      },{
        text: 'D. 테마파크',
        weight: 4
      }]
    },
  }];

  var results = [{
    id: 1,
    text:'result 1 text',
    minScore:0
  },{
    id: 2,
    text:'result 2 text',
    minScore:5
  },{
    id: 3,
    text:'result 3 text',
    minScore:9
  }];

  // QUIZ ENGINE
  function quiz() {
    var currentQuestion = 0; // default starting value
    var currentScore = 0; // default starting value
    var answerLog = [] // for storing answers for Marketo
    $quizProgress.attr("max", questions.length);
    $quizProgressDataLimit.html(questions.length);
    renderQuestion(currentQuestion);

    // RENDER
    function renderQuestion() {
      var question = questions[currentQuestion];
      var optionsHtml = [];
      var questionText = question.text;
      var questionOptionText = question.answers.options;
      $quizQuestionText.html(questionText);
      for(var i = 0; i < questionOptionText.length; i++) {
        if (question.answers.type == 'range'){
          var questionOptionItem = '<button class="quiz-opt range" value="'+questionOptionText[i].weight+'" id="'+questionOptionText[i].text+'">'+questionOptionText[i].text+'</button>'
        } else {
          var questionOptionItem = '<button class="quiz-opt" value="'+questionOptionText[i].weight+'" id="'+questionOptionText[i].text+'">'+questionOptionText[i].text+'</button>'
        }
        optionsHtml.push(questionOptionItem);
      }
      $quizQuestionOptions.html(optionsHtml.join(''));
      $('.quiz button').click(nextQuestion);
    } // END renderQuestion

    // HANDLER
    function nextQuestion() {
      currentQuestion += 1;
      var optionValue = parseInt(this.value);
      currentScore += optionValue;
      console.log('currentScore=', currentScore);
      $quizProgress.attr("value", currentQuestion);
      $quizProgressDataCurrent.html(currentQuestion);
      if (questions.length == currentQuestion){
        calculateResults();
      } else {
        renderQuestion();
        // addToAnswerLog();
      }
    } // END nextQuestion

    // RESULTS
    function calculateResults() {
      $('.quiz .question').html('<p class="questionText">결과 지도 api 나오는 곳</p>');
    }
  } // END quiz engine

  // Init render
  quiz();

} // END quizInit

$(function() {
  quizInit();
});

// MARKETO FORM INJECTION