$().ready(function(){
    get_leads();
})
$('#filter_name').keyup(function(){
    get_leads();
});
$('#filter_from').change(function(){
    get_leads();
});
$('#filter_to').change(function(){
    get_leads();
});
$('#results').on('click', '.page_link', function(e){
    e.preventDefault()
    page_num = $(this).attr('href')
    get_leads(page_num)
});


function get_leads(page_num=1){
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", window.CSRF_TOKEN);
            }
        }
    });

    $.ajax({
        url: '/ajaxpagination/get_leads/',
        method: 'post',
        data: getFilterData(page_num),
        success: function(serverResponse){
            console.log(serverResponse)
            $('#results').html(serverResponse)
            // $('#pagination').html(serverResponse)
        }
    })
}

function getFilterData(page_num) {
    var filters = $('.search_field')    

    return {
        name: filters[0].value,
        from_date: filters[1].value,
        to_date: filters[2].value,
        page: page_num
    }
}





function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}