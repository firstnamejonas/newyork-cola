# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes | Link |
| --- | --- | --- | --- | --- |
| home | index.html | ![screenshot](documentation/validation/html-validation-home.png) | Minor warning that doesn't requires any actions. | [Click here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnewyork-cola-c035d6287dfe.herokuapp.com%2F) |
| colas | all_colas.html | ![screenshot](documentation/validation/html-validation-products.png) | Minor warning that doesn't requires any actions. | [Click here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnewyork-cola-c035d6287dfe.herokuapp.com%2Fproducts%2F) |
| colas | product_page.html | ![screenshot](documentation/validation/html-validation-productspage.png) | Minor warning that doesn't requires any actions. | [Click here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnewyork-cola-c035d6287dfe.herokuapp.com%2Fproducts%2F4) |
| contact | contact_page.html | ![screenshot](documentation/validation/html-validation-contact.png) | The shown error is a known error. I changed the placeholder to 'None' in order to no trigger the bug if I delete the placeholder that triggers the error. | [Click here](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fnewyork-cola-c035d6287dfe.herokuapp.com%2Fcontact%2F) |
| promo | contest_page.html | ![screenshot](documentation/validation/html-validation-contest.png) | Minor warning that doesn't requires any actions. | [Click here](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fnewyork-cola-c035d6287dfe.herokuapp.com%2Fcontest%2F) |
| bag | bag.html | ![screenshot](documentation/validation/html-validation-bag.png) | Minor warning that doesn't requires any actions. | [Click here](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fnewyork-cola-c035d6287dfe.herokuapp.com%2Fbag%2F) |
| checkout | checkout.html | ![screenshot](documentation/validation/html-validation-checkout.png) | No errors or warnings to show. | [Click here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnewyork-cola-c035d6287dfe.herokuapp.com%2Fcheckout%2F) |
| checkout | checkout_success.html | ![screenshot](documentation/validation/html-validation-checkoutsuccess.png) | No errors or warnings to show. | [Click here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnewyork-cola-c035d6287dfe.herokuapp.com%2Fcheckout%2Fcheckout_success%2F1063805ACEA34789A360F34488620EAD) |
| userprofiles | userprofile.html | ![screenshot](documentation/validation/html-validation-profile.png) | Due to a non-document-error the live site of userprofile can't be checked via the HTML validator. I checked it with the text input option on the HTML validator and got no errors or warnings. | [Click here](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fnewyork-cola-c035d6287dfe.herokuapp.com%2Fuserprofile%2F) |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fnewyork-cola-c035d6287dfe.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=de) | ![screenshot](documentation/validation/css-validation-style.png) | Pass: No Errors |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| stripe_elements.js | ![screenshot](documentation/validation/js-validation-stripe.png) | Undefined Stripe variable |

