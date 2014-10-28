var mongoose = require('mongoose');

var outer_schema = mongoose.Schema({
	modes: [{type: mongoose.Schema.Types.ObjectId, ref: 'Inner'}]
});

var outer = mongoose.model('Outer', outer_schema);

module.exports = outer;