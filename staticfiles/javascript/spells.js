
/*Add spell AJAX*/
$(document).on('submit', '#add_spell_button', function(e){
    //Prevent form form being posted
    e.preventDefault();
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
            /*If spell needs to be added*/
            if ($.isEmptyObject(data) == false) {
                var spell_level = data.level;
                var part1 = '<div id= "added_spell_ajax" class = "my_spells_spell_name">';
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
                 $("#added_spell_ajax").css('font-size', '4vw');
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


/*Delete spell*/
$(document).ready(function(){
  $(".my_spells_spell_del").click(function(){
      var spell_name = $(this).siblings(".my_spells_spell_name");
      var spell_name_txt = $(this).siblings(".my_spells_spell_name").text();
      spell_name_Parent = spell_name.parent();
      answer = confirm("Are you sure you want to delete " + spell_name_txt + "?");
      if (answer == true) {
        $.ajax({
            type: 'POST',
            //go to this URL
            url: '/spells/deletelevel',
            //with this data
            data: {
            spell_name_key:spell_name_txt,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            //if view from url: '/spells/deletelevel/ succesfully performed, do the following
            success:function(data){
                spell_name_Parent.hide();
            }
        });
      }
  });
});


/*Preparation spell */

$(document).ready(function(){

    var timeout_id = 0;
    var hold_time = 1000;
    var hold_trigger = $('.my_spells_spell_name');
    var hold_trigger_name = '';
    var hold_trigger_id = '';
    var hold_trigger_status = '';

    /*Desktop*/
    hold_trigger.mousedown(function() {
        /*get name, id and color (aka status) of selected spell */
        hold_trigger_name = $(this).html();
        hold_trigger_id = $(this).attr('id');
        hold_trigger_color = $(this).css('color');
        timeout_id = setTimeout(function(){update_spell_status(hold_trigger_name,hold_trigger_id,hold_trigger_color);}, hold_time);
    /*when mouse leaves spell: reset timeout_id*/
    }).bind('mouseup mouseleave', function() {
        clearTimeout(timeout_id);});

    /*Mobile*/
    hold_trigger.bind("touchstart", function(e) {
        hold_trigger_name = $(this).html();
        hold_trigger_id = $(this).attr('id');
        hold_trigger_color = $(this).css('color');
        timeout_id = setTimeout(function(){update_spell_status(hold_trigger_name,hold_trigger_id,hold_trigger_color );}, hold_time);
    }).bind("touchend", function() {
        clearTimeout(timeout_id);});

});

function update_spell_status(hold_trigger_name,hold_trigger_id,hold_trigger_color) {
    $.ajax({
        type: 'POST',
        //go to this URL
        url: '/spells/preparationspell',
        //with this data
        data: {
            hold_trigger_name_key:hold_trigger_name,
            hold_trigger_color_key:hold_trigger_color,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        //if view from url: '/spells/preparationspell/ succesfully performed, do the following
        success:function(){
            /*Change color (preparation status) of spell*/
            hold_trigger_id_selector = $('#'+hold_trigger_id);
            if (hold_trigger_color.indexOf("0, 0, 0") >=  0) {
                hold_trigger_id_selector.css("color", "grey");
            }
            else {
                hold_trigger_id_selector.css("color", "black");
            }
        }
    });
}