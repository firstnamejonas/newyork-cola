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
| templates | signup.html | ![screenshot](documentation/validation/html-validation-signup.png) | No errors or warnings to show. | [Click here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnewyork-cola-c035d6287dfe.herokuapp.com%2Faccounts%2Fsignup%2F) |
| templates | login.html | ![screenshot](documentation/validation/html-validation-login.png) | No errors or warnings to show. | [Click here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnewyork-cola-c035d6287dfe.herokuapp.com%2Faccounts%2Flogin%2F) |
| templates | password_reset.html | ![screenshot](documentation/validation/html-validation-password-reset.png) | No errors or warnings to show. | [Click here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnewyork-cola-c035d6287dfe.herokuapp.com%2Faccounts%2Fpassword%2Freset%2F) |
| templates | password_reset_done.html | ![screenshot](documentation/validation/html-validation-password-reset-done.png) | No errors or warnings to show. | [Click here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnewyork-cola-c035d6287dfe.herokuapp.com%2Faccounts%2Fpassword%2Freset%2Fdone%2F) |
| templates | email.html | ![screenshot](documentation/validation/html-validation-email.png) | No errors or warnings to show. | [Click here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnewyork-cola-c035d6287dfe.herokuapp.com%2Faccounts%2Fconfirm-email%2F) |
| templates | email_confirm.html | ![screenshot](documentation/validation/html-validation-email-confirm.png) | No errors or warnings to show. | [Click here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnewyork-cola-c035d6287dfe.herokuapp.com%2Faccounts%2Fconfirm-email%2FOA%3A1s4mYf%3AMMLVHTyCUMBndWdtkFpZmnJnM4w1vq5N8FNLQ8LJEWs%2F) |
| templates | logout.html | ![screenshot](documentation/validation/html-validation-logout.png) | No errors or warnings to show. | [Click here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnewyork-cola-c035d6287dfe.herokuapp.com%2Faccounts%2Flogout%2F) |
| templates | add_cola.html | ![screenshot](documentation/validation/html-validation-add.png) | No errors or warnings to show. | [Click here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnewyork-cola-c035d6287dfe.herokuapp.com%2Faccounts%2Flogin%2F%3Fnext%3D%2Fproducts%2Fadd%2F) |
| templates | edit_cola.html | ![screenshot](documentation/validation/html-validation-edit.png) | No errors or warnings to show. | [Click here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fnewyork-cola-c035d6287dfe.herokuapp.com%2Faccounts%2Flogin%2F%3Fnext%3D%2Fproducts%2Fedit%2F2%2F) |

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
| bag.js | ![screenshot](documentation/validation/js-validation-bag.png) | Pass: No Warning or Errors |
| colas.js | ![screenshot](documentation/validation/js-validation-colas.png) | Pass: No Warning or Errors |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| App | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| Bag | --- | --- | --- | --- |
| --- | contexts.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/bag/contexts.py) | ![screenshot](documentation/validation/py-validation-bag-contexts.png) | No errors or warnings. |
| --- | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/bag/urls.py) | ![screenshot](documentation/validation/py-validation-bag-urls.png) | No errors or warnings. |
| --- | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/bag/views.py) | ![screenshot](documentation/validation/py-validation-bag-views.png) | No errors or warnings. |
| --- | bag_tools.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/firstnamejonas/newyork-cola/main/bag/templatetags/bag_tools.py) | ![screenshot](documentation/validation/py-validation-bag-bagtools.png) | No errors or warnings. |
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

| Browser | Home | Products | Product | Contest | Contact| Signup | Login | Bag | Checkout | Checkout-Success | Profile | Add / Edit Products | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/browser-chrome-home.png) | ![screenshot](documentation/browsers/browser-chrome-products.png) | ![screenshot](documentation/browsers/browser-chrome-product.png) | ![screenshot](documentation/browsers/browser-chrome-contest.png) | ![screenshot](documentation/browsers/browser-chrome-contact.png) | ![screenshot](documentation/browsers/browser-chrome-signup.png) | ![screenshot](documentation/browsers/browser-chrome-login.png) | ![screenshot](documentation/browsers/browser-chrome-bag.png) | ![screenshot](documentation/browsers/browser-chrome-checkout.png) | ![screenshot](documentation/browsers/browser-chrome-checkoutsuccess.png) | ![screenshot](documentation/browsers/browser-chrome-profile.png) | ![screenshot](documentation/browsers/browser-chrome-add-edit.png) | Works as expected |
| Firefox | ![screenshot](documentation/browsers/browser-firefox-home.png) | ![screenshot](documentation/browsers/browser-firefox-products.png) | ![screenshot](documentation/browsers/browser-firefox-product.png) | ![screenshot](documentation/browsers/browser-firefox-contest.png) | ![screenshot](documentation/browsers/browser-firefox-contact.png) | ![screenshot](documentation/browsers/browser-firefox-signup.png) | ![screenshot](documentation/browsers/browser-firefox-login.png) | ![screenshot](documentation/browsers/browser-firefox-bag.png) | ![screenshot](documentation/browsers/browser-firefox-checkout.png) | ![screenshot](documentation/browsers/browser-firefox-checkoutsuccess.png) | ![screenshot](documentation/browsers/browser-firefox-profile.png) | ![screenshot](documentation/browsers/browser-firefox-add-edit.png) | Works as expected |
| Safari | ![screenshot](documentation/browsers/browser-safari-home.png) | ![screenshot](documentation/browsers/browser-safari-products.png) | ![screenshot](documentation/browsers/browser-safari-product.png) | ![screenshot](documentation/browsers/browser-safari-contest.png) | ![screenshot](documentation/browsers/browser-safari-contact.png) | ![screenshot](documentation/browsers/browser-safari-signup.png) | ![screenshot](documentation/browsers/browser-safari-login.png) | ![screenshot](documentation/browsers/browser-safari-bag.png) | ![screenshot](documentation/browsers/browser-safari-checkout.png) | ![screenshot](documentation/browsers/browser-safari-checkoutsuccess.png) | ![screenshot](documentation/browsers/browser-safari-profile.png) | ![screenshot](documentation/browsers/browser-safari-add-edit.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | Products | Product | Contest | Contact| Signup | Login | Bag | Checkout | Checkout-Success | Profile | Add / Edit | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsiveness/responsive-mobile-home.png) | ![screenshot](documentation/responsiveness/responsive-mobile-products.png) | ![screenshot](documentation/responsiveness/responsive-mobile-product.png) | ![screenshot](documentation/responsiveness/responsive-mobile-contest.png) | ![screenshot](documentation/responsiveness/responsive-mobile-contact.png) | ![screenshot](documentation/responsiveness/responsive-mobile-signup.png) | ![screenshot](documentation/responsiveness/responsive-mobile-login.png) | ![screenshot](documentation/responsiveness/responsive-mobile-bag.png) | ![screenshot](documentation/responsiveness/responsive-mobile-checkout.png) | ![screenshot](documentation/responsiveness/responsive-mobile-checkoutsuccess.png) | ![screenshot](documentation/responsiveness/responsive-mobile-profile.png) | ![screenshot](documentation/responsiveness/responsive-mobile-add-edit.png) | Works as expected. |
| Tablet (DevTools) | ![screenshot](documentation/responsiveness/responsive-tablet-home.png) | ![screenshot](documentation/responsiveness/responsive-tablet-products.png) | ![screenshot](documentation/responsiveness/responsive-tablet-product.png) | ![screenshot](documentation/responsiveness/responsive-tablet-contest.png) | ![screenshot](documentation/responsiveness/responsive-tablet-contact.png) | ![screenshot](documentation/responsiveness/responsive-tablet-signup.png) | ![screenshot](documentation/responsiveness/responsive-tablet-login.png) | ![screenshot](documentation/responsiveness/responsive-tablet-bag.png) | ![screenshot](documentation/responsiveness/responsive-tablet-checkout.png) | ![screenshot](documentation/responsiveness/responsive-tablet-checkoutsuccess.png) | ![screenshot](documentation/responsiveness/responsive-tablet-profile.png) | ![screenshot](documentation/responsiveness/responsive-tablet-add-edit.png) | Works as expected. |
| Desktop | ![screenshot](documentation/browsers/browser-chrome-home.png) | ![screenshot](documentation/browsers/browser-chrome-products.png) | ![screenshot](documentation/browsers/browser-chrome-product.png) | ![screenshot](documentation/browsers/browser-chrome-contest.png) | ![screenshot](documentation/browsers/browser-chrome-contact.png) | ![screenshot](documentation/browsers/browser-chrome-signup.png) | ![screenshot](documentation/browsers/browser-chrome-login.png) | ![screenshot](documentation/browsers/browser-chrome-bag.png) | ![screenshot](documentation/browsers/browser-chrome-checkout.png) | ![screenshot](documentation/browsers/browser-chrome-checkoutsuccess.png) | ![screenshot](documentation/browsers/browser-chrome-profile.png) | ![screenshot](documentation/browsers/browser-chrome-add-edit.png) | Works as expected |
| IPhone13 | ![screenshot](documentation/responsiveness/responsive-iphone-home.png) | ![screenshot](documentation/responsiveness/responsive-iphone-products.png) | ![screenshot](documentation/responsiveness/responsive-iphone-product.png) | ![screenshot](documentation/responsiveness/responsive-iphone-contest.png) | ![screenshot](documentation/responsiveness/responsive-iphone-contact.png) | ![screenshot](documentation/responsiveness/responsive-iphone-signup.png) | ![screenshot](documentation/responsiveness/responsive-iphone-login.png) | ![screenshot](documentation/responsiveness/responsive-iphone-bag.png) | ![screenshot](documentation/responsiveness/responsive-iphone-checkout.png) | ![screenshot](documentation/responsiveness/responsive-iphone-checkoutsuccess.png) | ![screenshot](documentation/responsiveness/responsive-iphone-profile.png) | ![screenshot](documentation/responsiveness/responsive-iphone-add-edit.png) | Works as expected. |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

> [!NOTE]  
> The brand's corporate design results in minimal warnings in the accessibility category in Lighthouse Testing.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/lighthouse-home-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | Some minor warnings on best practice due to stripe and cloudinary. Low page load is a known issue with lighthouse using different internet accesses. |
| Products | ![screenshot](documentation/lighthouse/lighthouse-products-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-products-desktop.png) | Some minor warnings on best practice due to stripe and cloudinary. |
| Product | ![screenshot](documentation/lighthouse/lighthouse-product-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-product-desktop.png) | Some minor warnings on best practice due to stripe and cloudinary. |
| Contest | ![screenshot](documentation/lighthouse/lighthouse-contest-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-contest-desktop.png) | Some minor warnings on best practice due to stripe and cloudinary. |
| Contact | ![screenshot](documentation/lighthouse/lighthouse-contact-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-contact-desktop.png) | Some minor warnings on best practice due to stripe and cloudinary. Accessibility warnings due to the select element on the form. |
| Bag | ![screenshot](documentation/lighthouse/lighthouse-bag-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-bag-desktop.png) | Some minor warnings on best practice due to stripe and cloudinary. |
| Checkout | ![screenshot](documentation/lighthouse/lighthouse-checkout-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-checkout-desktop.png) | Some minor warnings on best practice due to stripe and cloudinary. Accessibility warnings due to the select element on the form. |
| Checkout-Success | ![screenshot](documentation/lighthouse/lighthouse-checkoutsuccess-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-checkoutsuccess-desktop.png) | Some minor warnings on best practice due to stripe and cloudinary. |
| Signup | ![screenshot](documentation/lighthouse/lighthouse-signup-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-signup-desktop.png) | Some minor warnings on best practice due to stripe and cloudinary. |
| Login | ![screenshot](documentation/lighthouse/lighthouse-login-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-login-desktop.png) | Some minor warnings on best practice due to stripe and cloudinary. |
| Profile | ![screenshot](documentation/lighthouse/lighthouse-profile-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-profile-desktop.png) | Some minor warnings on best practice due to stripe and cloudinary. Accessibility warnings due to the select element on the form. |
| Add / Edit | ![screenshot](documentation/lighthouse/lighthouse-add-edit-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-add-edit-desktop.png) | Some minor warnings on best practice due to stripe and cloudinary. |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail |
| --- | --- | --- | --- |
| All Pages (Navbar) | --- | --- | --- |
|  | User clicks on Logo | User gets redirected to the Home page. | Pass |
|  | User clicks on Home Link | User gets redirected to the Home page. | Pass |
|  | User clicks on Products Link | User gets redirected to the Products page. | Pass |
|  | User clicks on Contest Link | User gets redirected to the Contest page. | Pass |
|  | User clicks on Contact Link | User gets redirected to the Contact page. | Pass |
|  | User clicks on User Dropdown Menu | Dropdown opens up. If user is logged in, the menu displays links to the userprofile page or the logout page. If user in not logged in, the menu displays links to the signup or login page. If user clicks on the links he's redirected to the page accordingly. | Pass |
|  | User clicks on 'Buy Now' Link | User gets redirected to the Products page. | Pass |
|  | User clicks on Shopping Bag Link | User gets redirected to the Shopping Bag page. | Pass |
|  | User adds item to the Shopping Bag | Amount of the shopping bag updates accordingly. | Pass |
| All Pages (Messages) | --- | --- | --- |
|  | User triggers special messages events | User receives messages on the top of the page. | Pass |
| All Pages (Footer) | --- | --- | --- |
|  | User clicks on 'Github Icon' Link | User gets redirected to Github in a new tab. | Pass |
|  | User clicks on 'LinkedIn Icon' Link | User gets redirected to LinkedIn in a new tab. | Pass |
| Multiple Pages (Socials Section) | --- | --- | --- |
|  | User clicks on 'Instagram Icon' Link | User gets redirected to Instagram in a new tab. | Pass |
|  | User clicks on 'TikTok Icon' Link | User gets redirected to TikTok in a new tab. | Pass |
|  | User clicks on 'Twitter / X Icon' Link | User gets redirected to Twitter / X in a new tab. | Pass |
|  | User clicks on 'YouTube Icon' Link | User gets redirected to YouTube in a new tab. | Pass |
| Home | --- | --- | --- |
|  | User clicks on 'Find out more' Link | User's navigated to the about section to the Home page. | Pass |
|  | User clicks on 'Buy Now!' Links | User gets redirected to the Products page. | Pass |
|  | User clicks on 'Enter Now' Links | User gets redirected to the Contest page. | Pass |
|  | User clicks on 'Buy Now!' Links | User gets redirected to the Products page. | Pass |
|  | User tries to submit empty Newsletter form | Form can't be submitted, Error Message | Pass |
|  | User submits completed Newsletter form | User receives success message at the top of the Home page. | Pass |
| Products | --- | --- | --- |
|  | User clicks on 'Buy Now!' Links | User gets redirected to the according Product page. | Pass |
| Product | --- | --- | --- |
|  | User adjusts quantity of packages via quantity form field | Quantity of packages will be added to the shopping bag accordingly by clicking 'Add to bag' button. | Pass |
|  | User adjusts quantity of packages via quantity form field | Quantity of packages will be added to the shopping bag accordingly by clicking 'Add to bag' button. | Pass |
|  | User submits empty form field or 0. | User receives Server Error or Error Message. | Pass |
| Bag | --- | --- | --- |
|  | User clicks on 'Secure Checkout' Link | User gets redirected to the Checkout page. | Pass |
|  | User clicks on 'Keep Shopping' Link | User gets redirected to the Products page. | Pass |
|  | User adjusts quantity of packages via quantity form field and clicks on 'Update' | Bag total and all other neccessary information adjust accordingly. | Pass |
|  | User clicks on 'Remove' | Item is removed from the shopping bag. | Pass |
| Checkout | --- | --- | --- |
|  | User tries to submit checkout form without required information. | User receives error message and is informed which field to fill out. | Pass |
|  | User clicks on 'Adjust Bag' Link | User gets redirected to the Shopping Bag page. | Pass |
|  | User submits form via 'Complete Order' Button | User is redirected to the Checkout Success page. | Pass |
| Checkout Success | --- | --- | --- |
|  | User clicks on 'Win Free NYC Trip' Link | User gets redirected to the Contest page. | Pass |
| Profile | --- | --- | --- |
|  | User updates information via form. | New information displays in form after submitting. | Pass |
|  | User clicks on order number links. | User is redirected to the 'checkout success' page and can go back to the profile by clicking on the 'Back to Profile' link. | Pass |
| Allauth-Pages | --- | --- | --- |
|  | User tries to submit empty forms. | User receives error message with information what field is required. | Pass |
|  | User clicks on links such as 'sign up' (Login Page). | User gets redirected to the according page. | Pass |
| Contact | --- | --- | --- |
|  | User tries to submit empty forms. | User receives error message with information what field is required. | Pass |
| Contest | --- | --- | --- |
|  | User tries to submit empty forms. | User receives error message with information what field is required. | Pass |
| Add / Edit | --- | --- | --- |
|  | User wants to add a new project and uses the link that redirects him to the "Add new Product"-Form. | User gets redirected to page with the "Add new Product"-Form. | Pass |
|  | User tries to submit empty forms. | User receives error message with information what field is required. | Pass |
|  | User submits valid form. | New Product is added or a Product is updated depending on which form was submitted. | Pass |


## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a (new) site user, I would like to have access to general information about new york cola, so that I can get to know all important information about the product. | ![screenshot](documentation/features/feature-02-home.png) |
| As a (new) site user, I can easily find where to purchase The New York Cola products so that I can easily purchase the product without searching for a long time. | ![screenshot](documentation/features/feature-03-button.png) |
| As a (new) site user, I can view all information about the product on the product page, as well as selecting the packages I want to order, and add them to the shopping card so that I can purchase it later. | ![screenshot](documentation/features/feature-13-product.png) |
| As a (new) site user, I can view my shopping cart so that I can review my selected items before checkout. | ![screenshot](documentation/features/feature-12-bag.png) |
| As a (new) site user, I can proceed to checkout so that I can complete my purchase. | ![screenshot](documentation/features/feature-12-bag.png) |
| As a (new) site user, I can create an account so that I can save my information for future purchases. | ![screenshot](documentation/features/feature-11-profile.png) |
| As a (new) site user, I can remove items from my shopping cart so that I can eliminate unwanted products. | ![screenshot](documentation/features/feature-12-bag.png) |
| As a (new) site user, I can update the quantity of items in my shopping cart so that I can adjust my order as needed. | ![screenshot](documentation/features/feature-12-bag.png) |
| As a (new) site user, I can signup to a newsletter in order to receive messages on promos and more. | ![screenshot](documentation/features/feature-05-newsletter.png) |
| As a registered site user, I can log in to my account so that I can access my saved information. | ![screenshot](documentation/features/feature-11-profile.png) |
| As a registered site user, I can view and update my account information so that I can update my information in case I have a new address, etc. | ![screenshot](documentation/features/feature-11-profile.png) |
| As a registered site user, I can view my latest purchases so that I can keep track of what I've purchased. | ![screenshot](documentation/features/feature-11-profile.png) |
| As a returning site user, I can contact the company so that I can ask questions on my orders, get help, etc. | ![screenshot](documentation/features/feature-10-contact.png) |
| As an admin of the site, I can add, update and delete products so that I can manage the stores products easily on the frontend. | ![screenshot](documentation/browsers/browser-chrome-add-edit.png) ![screenshot](documentation/browsers/browser-chrome-delete.png)|

## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test name-of-app `

To create the coverage report, I would then run the following commands:

`coverage run --source=name-of-app manage.py test`

`coverage report`

Below are the results from the various apps on my application that I've tested:

| App | Coverage | Screenshot |
| --- | --- | --- |
| Bag | 99% | ![screenshot](documentation/tests/py-test-bag.png) |
| Checkout | 99% | ![screenshot](documentation/tests/py-test-checkout.png) |
| Home | 99% | ![screenshot](documentation/tests/py-test-home.png) |
| Colas | 99% | ![screenshot](documentation/tests/py-test-colas.png) |
| Contact | 99% | ![screenshot](documentation/tests/py-test-contact.png) |
| Promo | 89% | ![screenshot](documentation/tests/py-test-promo.png) |
| Userprofiles | 100% | ![screenshot](documentation/tests/py-test-userprofiles.png) |

## Bugs

| Bug | Screenshots | Solution | Screenshot |
| --- | --- | --- | --- |
| If user deleted the value in the quantity input field on the product page, the user received a Server Error 500. | ![screenshot](documentation/bugs/bug-03.png) | To fix this, I added the JavaScript Code you can see in the image on the side. With that I've forced the input to have a value and not trigger the Server Error 500. | ![screenshot](documentation/bugs/bug-03-solution.png) |
| Django Messages being displayed in the admin panel instead of the User Frontend | ![screenshot](documentation/bugs/bug-01.png) | To fix this, I added an if- and for-loop to the base template with some styling classes and html content. Now the messages are displayed on the top of the page directly under the navbar. | ![screenshot](documentation/bugs/bug-01-solution.png) |
| Ordered Items and Amount are not being displayed on Checkout Success Page and in the Admin Panel. | ![screenshot](documentation/bugs/bug-02.png) | To fix this, I added an order_line_item variable to the checkout view.  | ![screenshot](documentation/bugs/bug-02-solution.png) |

## Unfixed Bugs

> [!NOTE]  
> There are no remaining bugs that I am aware of.