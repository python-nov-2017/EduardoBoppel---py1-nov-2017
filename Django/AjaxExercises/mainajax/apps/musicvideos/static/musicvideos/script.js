$(document).ready(function(){
    
    $('#artist_search').submit(function(){
        
        $.post(
            $(this).attr('action'),
            $(this).serialize(),
            function(res) {
                var html_string = "";
                if (res.results.length !== 0) {
                    html_string = "<video controls src=" + res.results[0].previewUrl + "></video>";
                }
                else {
                    html_string = "Not Found";
                }
                $('#results').html(html_string);
            }, 'json' );
        return false;
        });
    });
        



// $(document).ready(function(){
    
//     $('#artist_search').submit(function(){    

//         console.log('searching')
//         var url="https://itunes.apple.com/search?term=";
//         url += $('#user_input').val();
//         url += "&entity=musicVideo";

//         console.log(url)

//         $.get(url, function(res) {
//             if (res.results.length !== 0) {
//                 html_string = "<video controls src=" + res.results[0].previewUrl + "></video>";
//                 console.log(html_string);
//             }
//             else {
//                 html_string = "Not Found";
//             }
//             $('#results').html(html_string);
//         }, 'json' );
//         return false;    
//     });
// });