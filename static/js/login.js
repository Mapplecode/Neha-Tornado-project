$('#login_btn').click(function(){

data = $('.reg-input')
var form ={}
for (let i = 0; i < data.length; i++) {
    var value = data[i]
    form[ data[i].id ] = data[i].value
  }
  let r = {
        url : '/login',
        type : 'POST',
        data : JSON.stringify(form),
        dataType: 'json',
        success : function(data){
        console.log(data)
        if(data.success == false){
        alert(data.message)
        }
        if(data.success == true){
        alert(data.message)
        document.location.href="/";
        }
        },
        error: function(){
        console.log('Error')
        }
    }
    $.ajax(r);

})