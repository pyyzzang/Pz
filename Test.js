//node Test.js

const request = require('request');
	
var message = { title : "title" , content : "content:", imgUrl : "imgUrl" , link : "link" }

request({
url : 'https://fcm.googleapis.com/fcm/send',
method : 'POST',
headers : {
	'Content-Type' : ' application/json',
	'Authorization' : 'key=AAAAajogzyI:APA91bHnRC7pY2kauGvz42eONKn6RfFJ-99YcX7UG4IbdIoyQVvaG0jTGApcwA1cmJW3VQ6QGHIOhdG8zuAeaUXu2Tc7HRpccD4lXiAHglg-Ciivt4dBWKjjE7JUUt_9ia8jXJGzcCxn'
},
body : JSON.stringify({
	"data" : {
	"message" : message
	},
	"to" : "dtXl3Z8bSoA:APA91bF-UJ3-XCtfcj4BCE6yQA9JStrHo0qeBytOElVXGplg4bBxFMzmAJtmnMuwr_U9F3kAXowqGU3z5NbbMC2Psk8KQts256EE_8r03th3KcNP8eoZWvpW9wT6BdygNR9BUfYgWcGI"
})
}, function(error, response, body) {
if (error) {
	console.error(error, response, body);
} else if (response.statusCode >= 400) {
	console.error('HTTP Error: ' + response.statusCode + ' - '
	+ response.statusMessage + '\n' + body);
	} else {
	console.log('Done')
	}
});