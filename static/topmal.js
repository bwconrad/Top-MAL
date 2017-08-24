(function($){
	$.fn.displayList = function(data){
		//$(this).html("<p>" + "Hello" + "</p>");

		var entryData = data.split(",");
		var i;
		for(i = 0; i < (entryData.length)/5; i++){
			var newEntry = addEntrytoTemplate(entryData[(5*i)], entryData[(5*i)+1], entryData[(5*i)+2], entryData[(5*i)+3], entryData[(5*i)+4], i);
		}
	}

	$.fn.addEntrytoTemplate = function(name, score, id, members, image, rank){
		
	}
})(jQuery);

$(document).ready(function(){
	
    $('#submit').on('click', function(){
        $.getJSON('/result', {'nitems': 3}, function(data) {
            $('#data').displayList(data)
        });
    });

    $('#alltime').on('click', function(){
       	var year = new Date();
    	$('#startYear').val(1917);
    	$('#endYear').val(year.getFullYear());
    });
});