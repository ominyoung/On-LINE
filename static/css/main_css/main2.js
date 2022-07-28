/*메인 테마 추천 js*/
$(document).ready(function() {
  var chld = $('.nt-homeunit__list').children();
  var curr = 0;
  var left = $('.ctrl-left');
  var rite = $('.ctrl-rite');

  if (chld.length < 7) {
    var temp = [];

    while(temp.length < 7) {
      $(chld).each(function() {
        var itm = $(this).clone();
        temp.push(itm);
      });
    }

    chld = temp;

    $('.nt-homeunit__list').append(chld);
  }

  // INITIALIZE
  var init = function(curr) {
    var _l1 = (curr === 0) ? chld.length - 1 : curr - 1;
    var _l2 = (_l1 === 0) ? chld.length - 1 : _l1 - 1;
    var _l3 = (_l2 === 0) ? chld.length - 1 : _l2 - 1;

    var _r1 = (curr === chld.length - 1) ? 0 : curr + 1;
    var _r2 = (_r1 === chld.length - 1) ? 0 : _r1 + 1;
    var _r3 = (_r2 === chld.length - 1) ? 0 : _r2 + 1;

    $(chld[curr]).addClass('curr');
    $(chld[_l1]).addClass('prev');
    $(chld[_l2]).addClass('init');
    $(chld[_l3]).addClass('pre-init');
    $(chld[_r1]).addClass('next');
    $(chld[_r2]).addClass('last');
    $(chld[_r3]).addClass('pos-last');

    $('.nt-homedata p').html("Slide atual: " + curr);
  };

  init(curr);

  left.click(function(e) {
    e.preventDefault();

    curr = (curr === 0) ? chld.length - 1 : curr - 1;
    $(chld).each(function() {
      $(this).removeClass('curr');
      $(this).removeClass('prev');
      $(this).removeClass('pre-init');
      $(this).removeClass('init');
      $(this).removeClass('next');
      $(this).removeClass('last');
      $(this).removeClass('pos-last');
      init(curr);
    });
  });

  rite.click(function(e) {
    e.preventDefault();

    curr = (curr === chld.length - 1) ? 0 : curr + 1;

    $(chld).each(function() {
      $(this).removeClass('curr');
      $(this).removeClass('prev');
      $(this).removeClass('pre-init');
      $(this).removeClass('init');
      $(this).removeClass('next');
      $(this).removeClass('last');
      $(this).removeClass('pos-last');
      init(curr);
    });
  });
});