import React, { Component } from 'react';
import { render } from 'react-dom';
import MyForm from './surveyform';
import './style.css';

var $messages = $('.messages-content'),
    d, h, m,
    i = 0;

$(window).load(function() {
  $messages.mCustomScrollbar();
  setTimeout(function() {
    //fakeMessage();
  }, 100);
});

var cfInstance = ConversationalForm.startTheConversation({
  formEl: document.getElementById('cf-questions').appendTo($('.mCSB_container')).addClass('new');
  setDate();
  updateScrollbar();
});


function updateScrollbar() {
  $messages.mCustomScrollbar("update").mCustomScrollbar('scrollTo', 'bottom', {
    scrollInertia: 10,
    timeout: 0
  });
}

function setDate(){
  d = new Date()
  if (m != d.getMinutes()) {
    m = d.getMinutes();
    $('<div class="timestamp">' + d.getHours() + ':' + m + '</div>').appendTo($('.message:last'));
  }
}

function startTheconversation(){
  formE1 =$('.cf-questions').val();
  $('<div class="message message-personal">' + formEl + '</div>').document.getElementById('surveyform.cf-questions').appendTo($('.mCSB_container')).addClass('new');
setDate();
$('.message-input').val('null');
  updateScrollbar();
	interact(formE1);
  setTimeout(function() {
    //fakeMessage();
  }, 1000 + (Math.random() * 20) * 100);
}

$('.message-submit').click(function() {
  startTheConversation();
});

$(window).on('keydown', function(e) {
  if (e.which == 13) {
    insertMessage();
    return false;
  }
})
}

function insertMessage() {
  msg = $('.message-input').val();
  if ($.trim(msg) == '') {
    return false;
  }
  $('<div class="message message-personal">' + msg + '</div>').appendTo($('.mCSB_container')).addClass('new');
  setDate();
  $('.message-input').val(null);
  updateScrollbar();
	interact(msg);
  setTimeout(function() {
    //fakeMessage();
  }, 1000 + (Math.random() * 20) * 100);
}

$('.message-submit').click(function() {
  insertMessage();
});

$(window).on('keydown', function(e) {
  if (e.which == 13) {
    insertMessage();
    return false;
  }
})


function interact(message){
	// loading message
  $('<div class="message loading new"><figure class="avatar"><img src="/static/res/Cam2.png" /></figure><span></span></div>').appendTo($('.mCSB_container'));
    // make a POST request [ajax call]
	$.post('/message', {
		msg: message,
	}).done(function(reply) {
		// Message Received
		// 	remove loading meassage
    $('.message.loading').remove();
		// Add message to chatbox
    $('<div class="message new"><figure class="avatar"><img src="/static/res/Cam2.png" /></figure>' + reply['text'] + '</div>').appendTo($('.mCSB_container')).addClass('new');
    setDate();
    updateScrollbar();

		}).fail(function() {
				alert('error calling function');
				});
}
