// using jQuery
var okResponse=null, loginName=null, loginPicture=null;

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function getUserAuthStatus(response) {
    okResponse = response.status;
    return response.status;
}

function getChangedStatus(){

    return okResponse;
}
function getUserInfo(){
      FB.api(
      '/me',
      'GET',
      {"fields":"id,name"},
      function(response) {
          loginName=response.name;  
      });
    };

function getUserPicture(){
      FB.api("/me/picture",
      {"type":"small"},
      function(response) {
        if (response && !response.error) {
          loginPicture=response.data.url;
        }
         
      });
    };

function getUserName(){
    return loginName;
}    

function getPicture(){
    return loginPicture;
}