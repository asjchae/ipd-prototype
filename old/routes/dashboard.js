var mongoose = require('mongoose');
var Inner = require('../models/inner');
var Outer = require('../models/outer');

exports.add_student = function(req, res) {
	res.render('add-student', {title: 'Add A Student'})
};

exports.add_student_post = function(req, res) {
	console.log("Student added");
};