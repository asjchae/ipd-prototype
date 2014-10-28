var mongoose = require('mongoose');

var inner_schema = mongoose.Schema({
	messages: Array
});

var inner = mongoose.model('Inner', inner_schema);

module.exports = inner;