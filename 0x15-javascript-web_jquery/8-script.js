$.ajax({
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",
    method: "GET",
    dataType: "json",
    success: function(data) {
	let movies = data.results;
	$.each(movies, function(index, movie) {
	    $("UL#list_movies").append("<li>" + movie.title + "</li>");
	});
    },
    error: function(xhr, status, error) {
	console.log(xhr.statusText)
    }
});
