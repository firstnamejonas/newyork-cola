// Force qty_input to only be 0-99
$(".qty_input").on('input', function() {
    let inputVal = parseInt($(this).val());
    if (isNaN(inputVal) || inputVal < 0 || inputVal > 99) {
        $(this).val($(this).attr("min"));
    } else {
        $(this).val(inputVal);
    }
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