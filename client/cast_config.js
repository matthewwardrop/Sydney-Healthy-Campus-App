/*
 * This file is for you to configure your views. This is a sample configuration
 * file. You can use: $CAST to get instance of object. Functions may use 'this'
 * if they are attached to the $CAST object.
 */

$CAST.CONFIG.SERVER = "http://192.168.0.13/cast/";
$CAST.CONFIG.SCRIPT = "cast.cgi";
$CAST.CONFIG.INIT_QUERY = [null,{'init':true}];
//$CAST.CONFIG.INIT_QUERY = ["script",{'factory':'test','init':true}];

$CAST.CONFIG.init = function() {
	var loadingDiv = document.createElement("div");
	loadingDiv.setAttribute("id","loading");
	document.body.appendChild(loadingDiv);
	
	var topDiv = document.createElement("div");
	topDiv.setAttribute("id","top");
	
	var titleDiv = document.createElement("div");
	titleDiv.setAttribute("id","title");
	topDiv.appendChild(titleDiv);
	
	var userDiv = document.createElement("div");
	userDiv.setAttribute("id","user");
	topDiv.appendChild(userDiv);
	
	var spacer= document.createElement("span");
	topDiv.appendChild(spacer);
	document.body.appendChild(topDiv);
	
	var stackDiv = document.createElement("div");
	stackDiv.setAttribute("id","stack");
	document.body.appendChild(stackDiv);
	
	var bodyDiv = document.createElement("div");
	bodyDiv.setAttribute("id","content");
	bodyDiv.style.background = "#eee";
	bodyDiv.style.position = "relative";
	document.body.appendChild(bodyDiv);
	
	this.onResize();
	
	function loading(status) {
		if (status == "start") {
			$("#loading").show();
		} else {
			$("#loading").fadeOut();
		}
	}
	
	this.parent.addEventListener(this.onResize,["resize"]);
	this.parent.addEventListener(loading,["loading"]);
	
	/* Set default parameters */
	$CAST.preference('weight',70.0);
	$CAST.preference('height',1.8);
	$CAST.preference('gender','male');
	$CAST.preference('yob',1988);
	$CAST.preference('activity',1.4);
};

$CAST.CONFIG.onResize = function() {
	$("#title").width($(document).width()-$("#user").outerWidth());
	$("#stack").width($(document).width());
	$("#content").height($(document).height() - $("#top").outerHeight() - $("#stack").outerHeight());
	$("#loading").width($(document).width());
	$("#loading").height($("#content").outerHeight());
	$CAST.notifyEvent("render_complete");
};

$CAST.CONFIG.DEFAULT_DISPLAY = {
	layout: {user:false},
	app_title: "Healthy Campus",
	title: '&lt;title&gt;',
	stack: ['stack',{}],
	window_title: "Healthy Campus App",
	content: ""
};

$CAST.reLayout = function (cast,opts) {
	if (opts.title != false) {
		$("#title").show();
	} else {
		$("#title").hide();
	}
	if (opts.user) {
		$("#user").attr("onclick","$CAST.runAction(['pop',{}]);");
	} else {
		$("#user").attr("onclick","$CAST.runAction(['push',{'query':{'module':'profile'}}]);");
	}
	
};

$CAST.window_title = function (cast,opts) {
	window.document.title = opts;
};

$CAST.CONFIG.RENDER_HANDLERS = {
	"layout": $CAST.reLayout,
	"window_title": $CAST.window_title,
	"app_title": "title",
	"content": "content",
	"stack": "stack"
};

$CAST.CONFIG.OFFLINE_SHEETS = {
	
};

$CAST.CONFIG.LOCAL_METHODS = new Object();

$CAST.CONFIG.LOCAL_METHODS.pref = function (cast,pref) {
	return cast.preference(pref);
};

$CAST.CONFIG.LOCAL_METHODS.percentEER = function (cast,kj) {
	var weight = $CAST.preference('weight');
	var gender = $CAST.preference('gender');
	var yob = $CAST.preference('yob');
	var af = $CAST.preference('activity');
	var bmr_val = bmr(new Date().getFullYear() - yob,gender == 'male' ? 0 : 1, weight);
	var eer_val = eer(bmr_val,af);
	return (kj/eer_val*100).toFixed(1) ;
};

$CAST.CONFIG.LOCAL_METHODS.percentProtein = function (cast,grams) {
	var weight = $CAST.preference('weight');
	var gender = $CAST.preference('gender');
	var rp_val = rp(weight,gender == 'male' ? 0 : 1);
	return (grams/rp_val*100).toFixed(1) ;
};

$CAST.CONFIG.LOCAL_METHODS.percentTotalFat = function (cast,grams) {
	var weight = $CAST.preference('weight');
	var gender = $CAST.preference('gender');
	var yob = $CAST.preference('yob');
	var af = $CAST.preference('activity');
	var bmr_val = bmr(new Date().getFullYear() - yob,gender == 'male' ? 0 : 1, weight);
	var rtf_val = rtf(bmr_val,af);
	return (grams/rtf_val*100).toFixed(1) ;
};

$CAST.CONFIG.LOCAL_METHODS.percentSatFat = function (cast,grams) {
	var weight = $CAST.preference('weight');
	var gender = $CAST.preference('gender');
	var yob = $CAST.preference('yob');
	var af = $CAST.preference('activity');
	var bmr_val = bmr(new Date().getFullYear() - yob,gender == 'male' ? 0 : 1, weight);
	var rsf_val = rsf(bmr_val,af);
	return (grams/rsf_val*100).toFixed(1) ;
};

$CAST.CONFIG.LOCAL_METHODS.percentCarbohydrates = function (cast,grams) {
	var weight = $CAST.preference('weight');
	var gender = $CAST.preference('gender');
	var yob = $CAST.preference('yob');
	var af = $CAST.preference('activity');
	var bmr_val = bmr(new Date().getFullYear() - yob,gender == 'male' ? 0 : 1, weight);
	var rch_val = rch(bmr_val,af);
	return (grams/rch_val*100).toFixed(1) ;
};

$CAST.CONFIG.LOCAL_METHODS.percentSodium = function (cast,mgrams) {
	var rs_val = rs();
	return (mgrams/rs_val*100).toFixed(1) ;
};

$CAST.CONFIG.DEFAULT_FACTORY = "test";

$CAST.CONFIG.FACTORIES.test = function (opts) {
	return {'title':"Test Factory"}
}
