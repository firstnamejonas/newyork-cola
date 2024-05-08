/* jshint esversion: 11, jquery: true */

// Update quantity on click
$('.update-link').click(function(e) {
    e.preventDefault(); // Prevent the default form submission

    // Get the input element associated with the update link
    var inputField = $(this).siblings('.update-form').find('.qty_input');
    
    // Get the value of the input field
    var inputValue = inputField.val().trim();
    
    // Check if the input value is empty, not a number, or out of range
    if(inputValue === '' || isNaN(inputValue) || inputValue < 1 || inputValue > 99) {
        // Set a default value or handle the error as per your requirement
        inputField.val('1');
    } else {
        // If the input value is valid, submit the form
        var form = $(this).prev('.update-form');
        form.submit();
    }
});

// Remove item and reload on click
$('.remove-item').click(function(e) {
    var csrfToken = "{{ csrf_token }}";
    var itemId = $(this).attr('id').split('remove_')[1];
    var url = `/bag/delete/${itemId}/`;
    var data = {'csrfmiddlewaretoken': csrfToken};

    $.post(url, data)
        .done(function() {
            location.reload();
        });
});

// Increment quantity
$('.qty-increment').click(function(e) {
    e.preventDefault(); // Prevent the default button behavior
    
    // Get the input element associated with the increment button
    var inputField = $(this).closest('.input-group').find('.qty_input');
    
    // Get the current value of the input field
    var currentValue = parseInt(inputField.val().trim());
    
    // Increment the value if it's within the range
    if(!isNaN(currentValue) && currentValue < 99) {
        inputField.val(currentValue + 1);
    }
});

// Decrement quantity
$('.qty-decrement').click(function(e) {
    e.preventDefault(); // Prevent the default button behavior
    
    // Get the input element associated with the decrement button
    var inputField = $(this).closest('.input-group').find('.qty_input');
    
    // Get the current value of the input field
    var currentValue = parseInt(inputField.val().trim());
    
    // Decrement the value if it's within the range
    if(!isNaN(currentValue) && currentValue > 1) {
        inputField.val(currentValue - 1);
    }
});