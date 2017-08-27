(function($){
	// Display response data in rankings
	$.fn.displayList = function(entries){

		for(i=0; i<entries.length; i++){
			var item = $('#entryTemplate').html(); // Copy 
			var template = $(item).clone();

            // Change entries with score 0 to N/A
			if(entries[i][1] == '0'){
				entries[i][1] = 'N/A'
			}

            // Add thouand separator commas to members
            entries[i][3] = $(this).addCommas(entries[i][3]);

			// Put in entry's data into the template
			$(template).find('.rank').html(i+1); 
			$(template).find('img').attr('src', entries[i][4]);
			$(template).find('.name').prop('href', 'https://myanimelist.net/anime/' + entries[i][2]);
			$(template).find('.name').html(entries[i][0]);
			$(template).find('.season').html(entries[i][5]);
			$(template).find('.type').html(entries[i][6]);
			$(template).find('.score').html(entries[i][1]); 
			$(template).find('.members').html(entries[i][3]); 

			$('.rankingTable').append(template); // Append to bottom of ranking
		}	
	}
	
    $.fn.addCommas = function(num){
        num += '';
        x = num.split('.');
        x1 = x[0];
        x2 = x.length > 1 ? '.' + x[1] : '';
        var rgx = /(\d+)(\d{3})/;
        while (rgx.test(x1)) {
                x1 = x1.replace(rgx, '$1' + ',' + '$2');
        }
        return x1 + x2;
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
    	$("#submit").css("pointer-events", "none"); // Disable click until finshed
    	// Get form inputs
    	var searchData = $(this).getFormData();

    	// Validate form
   		if(!($(this).formValidation(searchData))){ 
   			$("#submit").css("pointer-events", "auto"); // Enable clicking
   			return false; // Invalid form
   		}

   		$(".rankingTable").html("<p><b>Getting Search Results</p>"); // Loading message

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
           	$(".rankingTable").html(""); // Before new search make sure rankings are clear
           	$('#data').displayList(data) // Show rankings
           	$("#submit").css("pointer-events", "auto"); // Enable clicking
        });    
    });

    $('#alltime').on('click', function(){
       	var year = new Date();
    	$('#startYear').val(1917);
    	$('#endYear').val(year.getFullYear());    	
    });
});