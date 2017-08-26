(function($){
	$.fn.displayList = function(data){
		//$(this).html("<p>" + "Hello" + "</p>");

		var entryData = data.split(",");
		var i;
		for(i = 0; i < (entryData.length)/5; i++){
			var newEntry = addEntrytoTemplate(entryData[(5*i)], entryData[(5*i)+1], entryData[(5*i)+2],
			entryData[(5*i)+3], entryData[(5*i)+4], i);
		}
	}

	$.fn.addEntrytoTemplate = function(name, score, id, members, image, rank){
		
	}

	// Get form values
	$.fn.getFormData = function(){
		// Sorting Type
		if($('#score').is(":checked")){
    		var sort = 'score';
    	}
    	else{
    		var sort = 'pop';
    	}

    	var start = $('#startYear').val(); // Start Year
    	var end = $('#endYear').val(); // End Year

    	// Tv
    	if($('#tv').is(":checked")){
    		var tv = 'true';
    	}

    	else{
    		var tv = 'false';
    	}

    	// Movie
    	if($('#movie').is(":checked")){
    		var movie = 'true';
    	}

    	else{
    		var movie = 'false';
    	}

    	// OVA
    	if($('#ova').is(":checked")){
    		var ova = 'true';
    	}

    	else{
    		var ova = 'false';
    	}

    	// ONA
    	if($('#ona').is(":checked")){
    		var ona = 'true';
    	}

    	else{
    		var ona = 'false';
    	}

    	// Special
    	if($('#special').is(":checked")){
    		var special = 'true';
    	}

    	else{
    		var special = 'false';
    	}

    	return [sort, start, end, tv, movie, ova, ona, special];
	}

	// Validate form values
	$.fn.formValidation = function(searchData){
		// Empty year box
		if(searchData[1] == "" || searchData[2] == ""){
			alert("Please fill in all values");
			return false;
		}
		// Integer year
		if(!(searchData[1] == parseInt(searchData[1], 10)) || !(searchData[2] == parseInt(searchData[2], 10))){
			alert("Please fill in only integer values");
			return false;
		}
		var year = new Date();
		// Outside of year range
		if(searchData[1] < 1917 || searchData[2] > year.getFullYear()){
			alert("Please input a range contained within 1917 to " + year.getFullYear());
			return false;
		}
		// StartYear > EndYear
		if(searchData[1]>searchData[2]){
			alert("Please make the From Year less than or equal to the To Year");
			return false;
		}
		// No types selected
		if(searchData[3] == 'false' && searchData[4] == 'false' && searchData[5] == 'false' &&
		    searchData[6] == 'false' && searchData[7] == 'false'){
			alert("Please select at least 1 anime type")
			return false;
		}
		return true
	}
	
})(jQuery);

$(document).ready(function(){

    $('#submit').on('click', function(){
    	var searchData = $(this).getFormData();

   		if(!($(this).formValidation(searchData))){ 
   			return false; // Invalid form
   		}

        $.getJSON('/result', 
        {
        	'sortby': searchData[0],
        	'start': searchData[1],
        	'end': searchData[2],
        	'tv': searchData[3],
        	'movie': searchData[4],
        	'ova': searchData[5],
        	'ona': searchData[6],
        	'special': searchData[7]
        }, 
        function(data) {
           	console.log(data);
           	//$('#data').displayList(data)
        });


    });

    $('#alltime').on('click', function(){
       	var year = new Date();
    	$('#startYear').val(1917);
    	$('#endYear').val(year.getFullYear());    	
    });
});