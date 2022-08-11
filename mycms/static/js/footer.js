window.addEventListener('load', (event) => {
    const questions = document.getElementsByClassName('faq-question')
    let answers = document.getElementsByClassName('faq-ans');
    for(let question of questions){
        question.addEventListener('click', show, false);
    }
});
  


function show(e){
    e.stopPropagation()
    let target = e.target.parentNode.nextElementSibling;
    let classlist = [...target.classList]
    let opened = document.getElementsByClassName('open');
    for(let answer of opened){
        if(answer !== target) {
            answer.classList.remove('open');
        }
        else{
            console.log(answer)
        }
        
    }

    // if(opened.length > 0){
    //     target.classList.toggle('open');
    //     target.classList.toggle('close');
    // }else{
    //     target.classList.toggle('open');
    // }
    // console.log(target)
    // target.style.display ="block"
    target.classList.toggle('open');
}