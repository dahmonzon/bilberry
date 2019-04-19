
let menu = document.querySelectorAll(".menu");

window.onload = function(){
    currentPageStyle();
};

function currentPageStyle(){
    const current = window.location.href;
    const menu = document.querySelectorAll(".menu");

   menu.forEach(element => {
       if(element.href === current ){
           console.log(element.href);
           console.log(current);
           element.classList.add("active");
       }
   });
}


