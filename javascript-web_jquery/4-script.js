#!/usr/bin/node

$(function () {
  $('#toggle_header').click(function() {
    if ($('header').hasClass('red')) {
      $('header').removeClass('red');
      $('header').addClass('green');
    } else {
      $('header').removeClass('green');
      $('header').addClass('red');
    }
  });
});
