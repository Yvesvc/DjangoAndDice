
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
            alert(data.message);
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


/*
function clickBarMobile() {
   var navBarElementsMobile = document.getElementById("nav_bar_elements_mobile");
   if (navBarElementsMobile.style.display === "none") {
   navBarElementsMobile.style.display = "block";
   }
   else {
   navBarElementsMobile.style.display = "none";
   }
}

var barInNavBar = document.getElementById("nav_bar_right_mobile");
barInNavBar.addEventListener("click", clickBarMobile);
*/