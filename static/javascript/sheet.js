
/* Position Features & Traits under Survival (Wis)*/
var survival = $('.skill_row_last');
var position = survival.offset();
$('.feat_trait').offset({
  top: position.top,
});


$('.feat_trait').css('padding-top', '7vh');


$('.feat_trait_val').css('position', 'absolute');
$('.feat_trait_val').css('width', '55vw');
/*$('.feat_trait_val').css('height', '35vh');*/
$('.feat_trait_val').css('margin-left', '2vw');

