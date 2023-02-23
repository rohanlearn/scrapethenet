(function ($) {
    $(function () {
  
      
  
    });
  })(jQuery);

 let message = document.querySelector('.text-message');

let text = 'Hello World !';
const speak = ()=>{
  
  message.textContent = "";
  for(let i = 0;i< text.length; i++){
    setTimeout(()=>{
      message.textContent += text[i];
    },i*100);
    if(i == text.length -1){
      setTimeout(()=>{
        mouth.style.animationPlayState = 'paused';
      },i*100)
    }
  }

}
speak();
setInterval(speak,3000);