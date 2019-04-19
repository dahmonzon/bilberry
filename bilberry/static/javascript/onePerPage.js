

function setImageAsReject(btn,images){
    url = "/img/treate/reject/"+ btn.id ;
        $.get(url, function (data,status) {
            url = "/img/oneItem/" + data ;
            document.location.href = url ;
          });
}

 
function setImageAsKeept(btn,images){
    
    url = "/img/treate/keept/"+ btn.id ;
        $.get(url, function (data,status) {
            url = "/img/oneItem/" + data ;
            document.location.href = url ;
          }); 
}

