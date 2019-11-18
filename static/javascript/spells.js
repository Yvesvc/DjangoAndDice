
/*Add spell AJAX*/
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
            var spell_level;
            spell_level = data.level
            if (spell_level.indexOf("Cantrip") >= 0) {
                alert('cantrip');
            }
            else if (spell_level.indexOf("1") >= 0){
                alert('1');
               }
            else if (spell_level.indexOf("2") >= 0){
                alert('2');
               }
            else if (spell_level.indexOf("3") >= 0){
                alert('3');
               }
            else if (spell_level.indexOf("4") >= 0){
                alert('4');
               }
            else if (spell_level.indexOf("5") >= 0){
                alert('5');
                $("#my_spells_lvl5").append(
                "<p>" +
                data.level +
                "</p>"
                );

               }
            else if (spell_level.indexOf("6") >= 0){
                alert('6');
               }
            else if (spell_level.indexOf("7") >= 0){
                alert('7');
               }
            else if (spell_level.indexOf("8") >= 0){
                alert('8');
               }
            else if (spell_level.indexOf("9") >= 0){
                alert('9');
               }
        }
    });
});

/* Show/hide my_spells info*/
$(document).ready(function(){
  $(".my_spells_spell").click(function(){
    if ( $(this).children(".my_spells_spell_info").css("display") == "none") {
        $(this).children(".my_spells_spell_info").show();
    }
    else {
        $(this).children(".my_spells_spell_info").hide();
    }
  });
});
