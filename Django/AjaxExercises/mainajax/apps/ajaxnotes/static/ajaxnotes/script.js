
// ADD NEW NOTE
$('#add_note_form').submit(function(e){
    e.preventDefault()
    $.ajax({
        url: $(this).attr('action'),
        method: $(this).attr('method'),
        data: $(this).serialize(),
        success: function(serverResponse){
            $('#notes').append(serverResponse)   
        }
    })
    $(this)[0].reset();
})

// DELETE NOTE
$('#notes').on('click', '.delete_note', function(e){
    e.preventDefault()
    $.ajax({
        url: $(this).attr('href'),
        method: 'get',
        success: function(serverResponse){
            $('#'+serverResponse).remove()
        }
    })
})

// SUBMIT DESCRIPTION AND HIDE FORM
$('#notes').on('submit', '.description_form', function(e){
    e.preventDefault()
    $.ajax({
        url: $(this).attr('action'),
        method: $(this).attr('method'),
        data: $(this).serialize(),
        success: function(serverResponse){
            $('#'+serverResponse['id']).find('.description_field').html(serverResponse['description']);
            $('#'+serverResponse['id']).find('.description_form').hide()
        }
    })
})

// SHOW DESCRIPTION FORM
$('#notes').on('click', '.description_field', function(){
    $(this).siblings('form').show()
})


