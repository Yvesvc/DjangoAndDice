
$(document).on('submit', '#Sheet_form', function(e){
    //Prevent form form being posted
    e.preventDefault();
    console.log('yes');
    $.ajax({
        type: 'POST',
        //go to this URL
        url: '/spells/addlevel',
        //with this data
        data: {
        name:$('#id_name').val(),
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        //if view from url: '/spells/addlevel/ succesfully performed, do the following
        success:function(data){
            alert('success');
            alert(data.message);
        }
    });
});