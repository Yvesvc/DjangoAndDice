
$(document).ready(function(){
/* Position Features & Traits under Survival (Wis)*/
var survival_position = $("#skill_row_last").offset();
$('.feat_trait').offset({
  top: survival_position.top,
});


$('.feat_trait').css('padding-top', '5.5vh');


$('.feat_trait_val').css('position', 'absolute');
$('.feat_trait_val').css('width', '65vw');
/*$('.feat_trait_val').css('height', '35vh');*/
$('.feat_trait_val').css('margin-left', '4vw');

$('.feat_trait_txt').css('width', '55vw');
$('.feat_trait_txt').css('font-size', '7pt');

});


