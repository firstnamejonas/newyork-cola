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
| templates | All Allauth Files | ![screenshot](documentation/validation/html-validation-allauth.png) | Representative for all other allauth templates I tested the signup template, since they‘re all based on the same structure. | [Click here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnewyork-cola-c035d6287dfe.herokuapp.com%2Faccounts%2Fsignup%2F) |

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

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| App | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| Bag | --- | --- | --- | --- |
| --- | contexts.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/bag/contexts.py) | ![screenshot](documentation/validation/py-validation-bag-contexts.png) | No errors or warnings. |
| --- | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/bag/urls.py) | ![screenshot](documentation/validation/py-validation-bag-urls.png) | No errors or warnings. |
| --- | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/bag/views.py) | ![screenshot](documentation/validation/py-validation-bag-views.png) | No errors or warnings. |
| Checkout | --- | --- | --- | --- |
| --- | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/checkout/admin.py) | ![screenshot](documentation/validation/py-validation-checkout-admin.png) | No errors or warnings. |
| --- | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/checkout/forms.py) | ![screenshot](documentation/validation/py-validation-checkout-forms.png) | No errors or warnings. |
| --- | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/checkout/models.py) | ![screenshot](documentation/validation/py-validation-checkout-models.png) | No errors or warnings. |
| --- | signals.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/checkout/signals.py) | ![screenshot](documentation/validation/py-validation-checkout-signals.png) | No errors or warnings. |
| --- | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/checkout/urls.py) | ![screenshot](documentation/validation/py-validation-checkout-urls.png) | No errors or warnings. |
| --- | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/checkout/views.py) | ![screenshot](documentation/validation/py-validation-checkout-views.png) | No errors or warnings. |
| Colas | --- | --- | --- | --- |
| --- | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/colas/admin.py) | ![screenshot](documentation/validation/py-validation-colas-admin.png) | No errors or warnings. |
| --- | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/colas/models.py) | ![screenshot](documentation/validation/py-validation-colas-models.png) | No errors or warnings. |
| --- | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/colas/urls.py) | ![screenshot](documentation/validation/py-validation-colas-urls.png) | No errors or warnings. |
| --- | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/colas/views.py) | ![screenshot](documentation/validation/py-validation-colas-views.png) | No errors or warnings. |
| Contact | --- | --- | --- | --- |
| --- | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/contact/admin.py) | ![screenshot](documentation/validation/py-validation-contact-admin.png) | No errors or warnings. |
| --- | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/contact/forms.py) | ![screenshot](documentation/validation/py-validation-contact-forms.png) | No errors or warnings. |
| --- | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/contact/models.py) | ![screenshot](documentation/validation/py-validation-contact-models.png) | No errors or warnings. |
| --- | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/contact/urls.py) | ![screenshot](documentation/validation/py-validation-contact-urls.png) | No errors or warnings. |
| --- | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/contact/views.py) | ![screenshot](documentation/validation/py-validation-contact-views.png) | No errors or warnings. |
| Home | --- | --- | --- | --- |
| --- | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/home/admin.py) | ![screenshot](documentation/validation/py-validation-home-admin.png) | No errors or warnings. |
| --- | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/home/forms.py) | ![screenshot](documentation/validation/py-validation-home-forms.png) | No errors or warnings. |
| --- | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/home/models.py) | ![screenshot](documentation/validation/py-validation-home-models.png) | No errors or warnings. |
| --- | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/home/urls.py) | ![screenshot](documentation/validation/py-validation-home-urls.png) | No errors or warnings. |
| --- | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/home/views.py) | ![screenshot](documentation/validation/py-validation-home-views.png) | No errors or warnings. |
| Promo | --- | --- | --- | --- |
| --- | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/promo/admin.py) | ![screenshot](documentation/validation/py-validation-promo-admin.png) | No errors or warnings. |
| --- | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/promo/forms.py) | ![screenshot](documentation/validation/py-validation-promo-forms.png) | No errors or warnings. |
| --- | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/promo/models.py) | ![screenshot](documentation/validation/py-validation-promo-models.png) | No errors or warnings. |
| --- | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/promo/urls.py) | ![screenshot](documentation/validation/py-validation-promo-urls.png) | No errors or warnings. |
| --- | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/promo/views.py) | ![screenshot](documentation/validation/py-validation-promo-views.png) | No errors or warnings. |
| Userprofiles | --- | --- | --- | --- |
| --- | admin.py | --- | --- | No code to be validated. |
| --- | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/userprofiles/forms.py) | ![screenshot](documentation/validation/py-validation-userprofiles-forms.png) | No errors or warnings. |
| --- | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/userprofiles/models.py) | ![screenshot](documentation/validation/py-validation-userprofiles-models.png) | No errors or warnings. |
| --- | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/userprofiles/urls.py) | ![screenshot](documentation/validation/py-validation-userprofiles-urls.png) | No errors or warnings. |
| --- | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/userprofiles/views.py) | ![screenshot](documentation/validation/py-validation-userprofiles-views.png) | No errors or warnings. |
| Main | --- | --- | --- | --- |
| --- | settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/main/settings.py) | ![screenshot](documentation/validation/py-validation-main-settings.png) | No errors or warnings. |
| --- | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/main/urls.py) | ![screenshot](documentation/validation/py-validation-main-urls.png) | No errors or warnings. |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | Products | Product | Contest | Contact| Signup | Login | Bag | Checkout | Checkout-Success | Profile | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/browser-chrome-home.png) | ![screenshot](documentation/browsers/browser-chrome-products.png) | ![screenshot](documentation/browsers/browser-chrome-product.png) | ![screenshot](documentation/browsers/browser-chrome-contest.png) | ![screenshot](documentation/browsers/browser-chrome-contact.png) | ![screenshot](documentation/browsers/browser-chrome-signup.png) | ![screenshot](documentation/browsers/browser-chrome-login.png) | ![screenshot](documentation/browsers/browser-chrome-bag.png) | ![screenshot](documentation/browsers/browser-chrome-checkout.png) | ![screenshot](documentation/browsers/browser-chrome-checkoutsuccess.png) | ![screenshot](documentation/browsers/browser-chrome-profile.png) | Works as expected |
| Firefox | ![screenshot](documentation/browsers/browser-firefox-home.png) | ![screenshot](documentation/browsers/browser-firefox-products.png) | ![screenshot](documentation/browsers/browser-firefox-product.png) | ![screenshot](documentation/browsers/browser-firefox-contest.png) | ![screenshot](documentation/browsers/browser-firefox-contact.png) | ![screenshot](documentation/browsers/browser-firefox-signup.png) | ![screenshot](documentation/browsers/browser-firefox-login.png) | ![screenshot](documentation/browsers/browser-firefox-bag.png) | ![screenshot](documentation/browsers/browser-firefox-checkout.png) | ![screenshot](documentation/browsers/browser-firefox-checkoutsuccess.png) | ![screenshot](documentation/browsers/browser-firefox-profile.png) | Works as expected |
| Safari | ![screenshot](documentation/browsers/browser-safari-home.png) | ![screenshot](documentation/browsers/browser-safari-products.png) | ![screenshot](documentation/browsers/browser-safari-product.png) | ![screenshot](documentation/browsers/browser-safari-contest.png) | ![screenshot](documentation/browsers/browser-safari-contact.png) | ![screenshot](documentation/browsers/browser-safari-signup.png) | ![screenshot](documentation/browsers/browser-safari-login.png) | ![screenshot](documentation/browsers/browser-safari-bag.png) | ![screenshot](documentation/browsers/browser-safari-checkout.png) | ![screenshot](documentation/browsers/browser-safari-checkoutsuccess.png) | ![screenshot](documentation/browsers/browser-safari-profile.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | Products | Product | Contest | Contact| Signup | Login | Bag | Checkout | Checkout-Success | Profile | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsiveness/responsive-mobile-home.png) | ![screenshot](documentation/responsiveness/responsive-mobile-products.png) | ![screenshot](documentation/responsiveness/responsive-mobile-product.png) | ![screenshot](documentation/responsiveness/responsive-mobile-contest.png) | ![screenshot](documentation/responsiveness/responsive-mobile-contact.png) | ![screenshot](documentation/responsiveness/responsive-mobile-signup.png) | ![screenshot](documentation/responsiveness/responsive-mobile-login.png) | ![screenshot](documentation/responsiveness/responsive-mobile-bag.png) | ![screenshot](documentation/responsiveness/responsive-mobile-checkout.png) | ![screenshot](documentation/responsiveness/responsive-mobile-checkoutsuccess.png) | ![screenshot](documentation/responsiveness/responsive-mobile-profile.png) | Works as expected. |
| Tablet (DevTools) | ![screenshot](documentation/responsiveness/responsive-tablet-home.png) | ![screenshot](documentation/responsiveness/responsive-tablet-products.png) | ![screenshot](documentation/responsiveness/responsive-tablet-product.png) | ![screenshot](documentation/responsiveness/responsive-tablet-contest.png) | ![screenshot](documentation/responsiveness/responsive-tablet-contact.png) | ![screenshot](documentation/responsiveness/responsive-tablet-signup.png) | ![screenshot](documentation/responsiveness/responsive-tablet-login.png) | ![screenshot](documentation/responsiveness/responsive-tablet-bag.png) | ![screenshot](documentation/responsiveness/responsive-tablet-checkout.png) | ![screenshot](documentation/responsiveness/responsive-tablet-checkoutsuccess.png) | ![screenshot](documentation/responsiveness/responsive-tablet-profile.png) | Works as expected. |
| Desktop | ![screenshot](documentation/browsers/browser-chrome-home.png) | ![screenshot](documentation/browsers/browser-chrome-products.png) | ![screenshot](documentation/browsers/browser-chrome-product.png) | ![screenshot](documentation/browsers/browser-chrome-contest.png) | ![screenshot](documentation/browsers/browser-chrome-contact.png) | ![screenshot](documentation/browsers/browser-chrome-signup.png) | ![screenshot](documentation/browsers/browser-chrome-login.png) | ![screenshot](documentation/browsers/browser-chrome-bag.png) | ![screenshot](documentation/browsers/browser-chrome-checkout.png) | ![screenshot](documentation/browsers/browser-chrome-checkoutsuccess.png) | ![screenshot](documentation/browsers/browser-chrome-profile.png) | Works as expected |
| IPhone13 | ![screenshot](documentation/responsiveness/responsive-iphone-home.png) | ![screenshot](documentation/responsiveness/responsive-iphone-products.png) | ![screenshot](documentation/responsiveness/responsive-iphone-product.png) | ![screenshot](documentation/responsiveness/responsive-iphone-contest.png) | ![screenshot](documentation/responsiveness/responsive-iphone-contact.png) | ![screenshot](documentation/responsiveness/responsive-iphone-signup.png) | ![screenshot](documentation/responsiveness/responsive-iphone-login.png) | ![screenshot](documentation/responsiveness/responsive-iphone-bag.png) | ![screenshot](documentation/responsiveness/responsive-iphone-checkout.png) | ![screenshot](documentation/responsiveness/responsive-iphone-checkoutsuccess.png) | ![screenshot](documentation/responsiveness/responsive-iphone-profile.png) | Works as expected. |