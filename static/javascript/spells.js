
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
            var part1 = '<div class = "my_spells_spell">';
            var part2 = '<div class = "my_spells_spell_info"> </div> </div>';
            if (spell_level.indexOf("Cantrip") >= 0) {
                $("#my_spells_lvl0").append(
                part1 + data.name + part2
                );
            }
            else if (spell_level.indexOf("1") >= 0){
                $("#my_spells_lvl1").append(
                part1 + data.name + part2
                );
               }
            else if (spell_level.indexOf("2") >= 0){
                $("#my_spells_lvl2").append(
                part1 + data.name + part2
                );
               }
            else if (spell_level.indexOf("3") >= 0){
                $("#my_spells_lvl3").append(
                part1 + data.name + part2
                );
               }
            else if (spell_level.indexOf("4") >= 0){
                $("#my_spells_lvl4").append(
                part1 + data.name + part2
                );
               }
            else if (spell_level.indexOf("5") >= 0){
                $("#my_spells_lvl5").append(
                part1 + data.name + part2
                );
               }
            else if (spell_level.indexOf("6") >= 0){
                $("#my_spells_lvl6").append(
                part1 + data.name + part2
                );
               }
            else if (spell_level.indexOf("7") >= 0){
                $("#my_spells_lvl7").append(
                part1 + data.name + part2
                );
               }
            else if (spell_level.indexOf("8") >= 0){
                $("#my_spells_lvl8").append(
                part1 + data.name + part2
                );
               }
            else if (spell_level.indexOf("9") >= 0){
                $("#my_spells_lvl9").append(
                part1 + data.name + part2
                );
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
