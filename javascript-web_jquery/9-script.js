#!/usr/bin/node

$(document).ready(function() {
  $.get('https://stefanbohacek.com/hellosalut/?lang=fr', function(data) {
    var hello = $(data).find('#hello').text();
    $('#hello').text(hello);
  });
});
