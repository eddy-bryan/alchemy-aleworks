# Alchemy Aleworks

![Responsive Design](../alchemy-aleworks/static/images/readme/responsive-design.png)

Welcome to Alchemy Aleworks, where craft beer meets alchemical inspiration. This platform celebrates the art of brewing through a diverse selection of finely crafted ales. Whether you're a seasoned beer enthusiast or a curious newcomer, Alchemy Aleworks offers a journey into the world of unique flavours and brewing traditions.

A link to the live website can be found [here](https://8000-eddybryan-alchemyalewor-2ri08eofcjg.ws.codeinstitute-ide.net/).

## Contents

- [Mission Statement](#mission-statement)
- [Business Model](#business-model)
- [User Experience](#user-experience)
    - [User Stories](#user-stories)
        - [Implemented User Stories](#implemented-user-stories)
        - [Future User Stories](#future-user-stories)
    - [Structure](#structure)
        - [Additional Pages](#additional-pages)
        - [Additional Features](#additional-features)
- [Agile Development Approach](#agile-development-approach)
- [Design Overview](#design-overview)
- [Technology Stack](#technology-stack)
- [Data Models](#data-models)
    - [Inventory](#inventory)
    - [Checkout](#checkout)
    - [Profiles](#profiles)
- [Features](#features)
- [Testing](#testing)
    - [User Stories Testing](#user-stories-testing)
    - [Unit Tests](#unit-tests)
    - [Debugging and Issue Resolution](#debugging-and-issue-resolution)
    - [Code Validator Checks](#code-validator-checks)
    - [Lighthouse](#lighthouse)
- [Deployment](#deployment)
- [Credits](#credits)

# Mission Statement

Alchemy Aleworks is dedicated to crafting exceptional beers that blend ancient alchemical wisdom with modern brewing techniques. Our platform serves as a haven for beer enthusiasts, offering a range of brews that evoke the spirit of alchemy in every sip. We aim to provide a welcoming environment where visitors can explore, discover, and savor the magic of our creations.

# Business Model

For detailed information on our e-commerce business model, please refer to the [Alchemy Aleworks E-commerce Business Model](../alchemy-aleworks/business_model.md).

# User Experience

The user experience on Alchemy Aleworks is designed to be immersive and informative. Visitors can easily navigate through our offerings, learn about our brewing process, and find their new favourite brew with ease.

## User Stories

### Target Audience

Alchemy Aleworks caters primarily to craft beer enthusiasts and those curious about unique brewing traditions. Our platform appeals to individuals who appreciate artisanal quality and seek to explore a variety of distinct beer flavours. Craft beer enthusiasts value authenticity, innovation, and the artistry behind brewing, while newcomers are eager to discover new tastes and experiences in the world of beer.

### Implemented User Stories

This section outlines the implemented user stories that reflect the functionality and features currently available on Alchemy Aleworks:

#### Navigation and Information

- As a visitor, I can view a list of available beers.
- As a visitor, I can view a list of available merchandise.
- As a visitor, I can view detailed information about each beer.
- As a visitor, I can view detailed information about each merchandise item.
- As a visitor, I can easily identify any deals, limited edition releases, or special offers.
- As a visitor, I can learn more about the brewery's story and values.
- As a visitor, I can find information about the taproom.

#### Registration and User Management

- As a user, I can easily log in or log out of my account.
- As a user, I can easily register for an account.
- As a user, I can subscribe to the brewery's newsletter.

#### Sorting, Searching, and Filtering

- As a visitor, I can sort the list of available beers.
- As a visitor, I can sort the list of available merchandise.
- As a visitor, I can search for specific beers or merchandise items by name or description.

#### Purchasing and Checkout

- As a customer, I can add items to my cart and proceed to checkout seamlessly.
- As a customer, I can have a smooth and secure checkout process.
- As a customer, I can easily select the quantity of a beer or merchandise item when making a purchase.
- As a customer, I can view my cart total and shipping costs before proceeding to checkout.
- As a customer, I can receive order confirmation after completing my purchase.

#### Admin and Store Management

- As an admin, I can add a new beer to the website.
- As an admin, I can update the details of an existing beer.
- As an admin, I can delete a beer from the website.
- As an admin, I can add a new merchandise item.
- As an admin, I can update the details of an existing merchandise item.
- As an admin, I can delete a merchandise item from the website.

#### Extra Features

- As a visitor, I can access the terms and conditions page.
- As a visitor, I can access the Returns and Delivery procedures page.
- As a visitor, I can access the privacy policy page.

### Future User Stories

Here, you'll discover user stories slated for future implementation in upcoming project updates. These stories outline prospective enhancements and potential new functionalities planned for the website:

- As a customer, I can receive personalised recommendations based on past purchases or preferences.

## Structure

Below, we present a combination of wireframe designs and screenshots showcasing various key pages of our website. This section provides a visual representation of our design process, from initial concepts to the final implemented interfaces.

### Home Page

#### Wireframe

![Home Page Wireframe](../alchemy-aleworks/static/images/readme/wireframes/homepage.png)

The wireframe outlines Alchemy Aleworks' homepage design, intended to feature key sections like the hero section with a compelling tagline and call-to-action buttons for shopping beers and merchandise, limited edition brews showcasing, taproom gallery images, a captivating story of the brewery, and a merchandise section.

#### Screenshot

![Home Page Screenshot](../alchemy-aleworks/static/images/readme/homepage.png)

The screenshot reflects the actual implementation of Alchemy Aleworks' homepage, closely mirroring the wireframe design. It includes:
- **Hero Section:** A visually striking image with overlaid text inviting visitors to explore the world of craft beers.
- **Limited Edition Brews:** Showcases randomoised selection of limited edition beers with descriptions of type and alcohol content, encouraging exploration and purchase.
- **Taproom Gallery:** Displays images of the taproom, enticing visitors to visit and experience it firsthand.
- **Our Story:** A narrative that captures the essence of Alchemy Aleworks' journey, blending historical inspiration with modern brewing techniques.
- **Merchandise Section:** Highlights a randomised selection of branded merchandise items, providing options for enthusiasts to show their support.

### Beers Page

#### Wireframe

![Beers Page Wireframe](../alchemy-aleworks/static/images/readme/wireframes/beers.png)

The wireframe illustrates the layout of Alchemy Aleworks' Beers page, designed to feature both the core range and limited edition beers. It includes sections for sorting options, beer cards displaying details such as name, type, alcohol content, and price, and navigation elements for user interaction.

#### Screenshot

![Beers Page Screenshot](../alchemy-aleworks/static/images/readme/beers.png)

The screenshot showcases the implemented Beers page of Alchemy Aleworks, closely resembling the wireframe design. Key elements include:
- **Core Range and Limited Edition Beers:** Displayed in separate sections with dedicated cards containing beer details and images.
- **Sorting Dropdown:** Allows users to sort beers by name, price, and alcohol content, enhancing user experience and ease of navigation.
- **Item Count:** Indicates the total number of beers displayed, providing transparency and helping users manage their browsing experience effectively.

### Beer Detail Page

#### Wireframe

![Beer Detail Page Wireframe](../alchemy-aleworks/static/images/readme/wireframes/beer-detail.png)

The wireframe illustrates the layout of Alchemy Aleworks' Beer Detail page, designed to showcase detailed information about a specific beer. It includes sections for displaying the beer's image, name, description, type, alcohol content, price, and an option to add the beer to the cart.

#### Screenshot

![Beer Detail Page Screenshot](../alchemy-aleworks/static/images/readme/beer-detail.png)

The screenshot showcases the implemented Beer Detail page of Alchemy Aleworks, closely resembling the wireframe design. Key elements include:
- **Beer Image:** Displayed prominently at the top of the page, providing a visual representation of the beer.
- **Beer Details:** Name, description, type, alcohol content, and price displayed clearly for user information.
- **Add to Cart Form:** Allows users to select the quantity and add the beer to their shopping cart, enhancing user interaction and facilitating purchases.
- **Superuser Options:** Links for superusers to edit or delete the beer, providing administrative control over the product catalog.
- **You Might Also Like Section:** Displays random beers that users might find interesting based on their current selection, encouraging further exploration of the product range.
- **Navigation:** Includes a link to return to the main Beers page, providing seamless navigation for users.

### Merchandise Page

#### Wireframe

![Merchandise Page Wireframe](../alchemy-aleworks/static/images/readme/wireframes/merch.png)

The wireframe illustrates the layout of Alchemy Aleworks' Merch page, designed to showcase various merchandise categories such as apparel & accessories and drinkware. It includes sections for sorting options, merchandise cards displaying details such as name and price, and navigation elements for user interaction.

#### Screenshot

![Merchandise Page Screenshot](../alchemy-aleworks/static/images/readme/merch.png)

The screenshot showcases the implemented Merch page of Alchemy Aleworks, closely resembling the wireframe design. Key elements include:

- **Merchandise Categories:** Displayed in distinct sections for apparel & accessories and drinkware, each featuring multiple merchandise items.
- **Sorting Options:** Dropdown menu allowing users to sort merchandise items by name ascending/descending or price ascending/descending.
- **Item Count:** Indicates the total number of merchandise items displayed, providing transparency and helping users manage their browsing experience effectively.

### Merchandise Detail Page

#### Wireframe

![Merchandise Detail Page Wireframe](../alchemy-aleworks/static/images/readme/wireframes/merch-detail.png)

The wireframe outlines the layout of Alchemy Aleworks' Merch Detail page, designed to provide comprehensive information about a specific merchandise item. It includes sections for displaying the item's image, name, description, price, size (if applicable), and an option to add the item to the cart.

#### Screenshot

![Merchandise Detail Page Screenshot](../alchemy-aleworks/static/images/readme/merch-detail.png)

The screenshot demonstrates the implemented Merch Detail page of Alchemy Aleworks, closely resembling the wireframe design. Key elements include:

- **Merchandise Image:** Featured prominently at the top of the page, providing a clear visual representation of the item.
- **Merchandise Details:** Name, description, price, and size (if applicable) displayed prominently for user information.
- **Add to Cart Form:** Allows users to select the quantity and add the item to their shopping cart, enhancing user interaction and facilitating purchases.
- **Superuser Options:** Links for superusers to edit or delete the merchandise item, providing administrative control over the product catalog.
- **You Might Also Like Section:** Displays random merchandise items that users might find appealing, encouraging further exploration of the product range.
- **Navigation:** Includes a link to return to the main Merch page, ensuring seamless navigation for users.

### Taproom Page

#### Wireframe

![Taproom Page Wireframe](../alchemy-aleworks/static/images/readme/wireframes/taproom.png)

The wireframe outlines the layout of Alchemy Aleworks' Taproom page, designed to encourage visitors to experience the brewery's taproom firsthand. It includes sections for taproom introduction, image gallery, opening times, and a map for location and directions.

#### Screenshot

![Taproom Page Screenshot](../alchemy-aleworks/static/images/readme/taproom.png)

The screenshot demonstrates the implemented Taproom page of Alchemy Aleworks, closely resembling the wireframe design. Key elements include:

- **Visit Our Taproom:** Introduction section inviting visitors to explore the brewery's taproom atmosphere and enjoy its craft beers.
- **Gallery Section:** Displays images that capture the ambiance and highlights of the taproom experience.
- **Taproom Opening Times:** Provides the weekly opening times schedule for visitors to plan their visit accordingly.
- **Map Section:** Includes an interactive map with location details and a link to get directions using Google Maps.

### About Page

#### Wireframe

![About Page Wireframe](../alchemy-aleworks/static/images/readme/wireframes/about.png)

The wireframe illustrates the layout of Alchemy Aleworks' About page, designed to tell the story of the brewery's journey from its humble beginnings to its current stature. It includes sections for introducing the brewery's history, showcasing images that capture its evolution, and featuring links to explore related content.

#### Screenshot

![About Page Screenshot](../alchemy-aleworks/static/images/readme/about.png)

The screenshot showcases the implemented About page of Alchemy Aleworks, closely resembling the wireframe design. Key elements include:

- **Our Story:** An introductory section that narrates the brewery's origins in a garage and its growth fueled by passion and experimentation.
- **From Garage to Greatness:** Continues the narrative, highlighting the transition from a garage setup to a fully equipped brewery, emphasising dedication to quality and creativity.
- **Gallery Section:** Displays images that visually represent key milestones and aspects of the brewery's journey.
- **Featured Beers:** Displays a selection of random beers, inviting visitors to explore the brewery's beers for sale.

### Additional Pages

#### Bag Page

- **Purpose:** Allows users to review and manage items added to their shopping bag or cart before proceeding to checkout.

![Bag Page Screenshot](../alchemy-aleworks/static/images/readme/bag.png)

#### Checkout Page

- **Purpose:** Allows users to review the items in their bag enter their delivery information and card details to purchase them. Users also have the option to securely store their delivery details to their profile, facilitating faster future purchases.

![Checkout Page Screenshot](../alchemy-aleworks/static/images/readme/checkout.png)

![Checkout Payment Screenshot](../alchemy-aleworks/static/images/readme/checkout-payment.png)

#### Accounts Pages

- **Purpose:** Enables users to authenticate themselves securely (login), create new accounts (signup), and securely log out from the website.

![Login Screenshot](../alchemy-aleworks/static/images/readme/login.png)

![Logout Screenshot](../alchemy-aleworks/static/images/readme/logout.png)

![Register Screenshot](../alchemy-aleworks/static/images/readme/register.png)

#### Profile Page

- **Purpose:** Stores and displays users' personal details, such as editable delivery information and interactive order history with the ability to view previous order confirmation pages.

![Profile Screenshot](../alchemy-aleworks/static/images/readme/profile.png)

#### Terms and Conditions / Privacy Policy / Delivery and Returns Pages

- **Purpose:** Offers users access to legal agreements and policies governing website usage, user data privacy, and product delivery and return terms.

![Login Screenshot](../alchemy-aleworks/static/images/readme/privacy-policy.png)

### Additional Features

#### Navigation Bar

- **Purpose:** The navigation bar enables seamless browsing across the website with intuitive menu options and dropdowns. It prominently showcases a centralised company logo and features interactive main menu options. On smaller devices, it transforms into a compact burger menu for ease of use. Additionally, it includes a secondary navigation menu with a search bar, account options (login/register/logout), and access for administrators to manage products. This menu also includes a shopping bag link that dynamically updates with a visible indicator, displaying the number of items currently in the user's bag.

![Navbar Large Screenshot](../alchemy-aleworks/static/images/readme/nav-large.png)

![Navbar Small Screenshot](../alchemy-aleworks/static/images/readme/nav-small.png)

#### Footer

- **Purpose:** Provides supplementary links and information such as contact details, social media links, and additional navigation menu items for enhanced user accessibility. Also privdes users with an option to sign up to the newsletter by inputting their email address into a form powered by MailChimp.

![Footer Screenshot](../alchemy-aleworks/static/images/readme/footer.png)

#### Age Verification Modal

- **Purpose:** Utilises cookies to display an age verification prompt upon site entry, ensuring compliance with age-related content restrictions due to sale of alcoholic products.

![Age Verification Modal Screenshot](../alchemy-aleworks/static/images/readme/age-check.png)

# Agile Development Approach

At Alchemy Aleworks, we embrace an Agile development approach to foster iterative improvement, flexibility, and collaboration with our stakeholders. This methodology allows us to continuously enhance our platform, adapt to evolving needs, and deliver value incrementally throughout the development lifecycle.

## User Story Labels

User stories in the Alchemy Aleworks project are categorised using different labels to prioritise features and functionalities. These labels are:

- **Must-Have**: Essential features critical for the core functionality of our e-commerce platform. These are foundational elements that must be implemented in the initial release to ensure a seamless user experience and operational efficiency.

- **Should-Have**: Important features that enhance user engagement, improve usability, or provide additional value. While not essential for the core functionality, these features significantly contribute to the overall user experience and satisfaction.

- **Could-Have**: Nice-to-have features that add supplementary value or convenience. These are considered low priority and may be deferred to future releases based on available time and resources.

- **Won't-Have**: Desirable features that are not immediately critical but are beneficial for future enhancements. These features can be considered for implementation if time and resources permit after addressing higher priority tasks.

### Must Have

![Must Have User Stories](../alchemy-aleworks/static/images/readme/user-stories/must-have.png)

### Should Have

![Should Have User Stories](../alchemy-aleworks/static/images/readme/user-stories/should-have.png)

### Could Have

![Could Have User Stories](../alchemy-aleworks/static/images/readme/user-stories/could-have.png)

### Won't Have

![Would Have User Stories](../alchemy-aleworks/static/images/readme/user-stories/wont-have.png)

The user stories outlined above represent our planned features categorised by priority. We aim to continuously iterate and enhance our platform based on these priorities, ensuring we deliver value incrementally while maintaining flexibility to adapt to future needs and feedback.

# Design Overview

The design of Alchemy Aleworks is a harmonious blend of aesthetic sophistication and functional simplicity, reflecting the artisanal quality of our craft beers. The website is designed to provide an engaging and intuitive user experience, appealing to both beer connoisseurs and casual visitors.

### Frameworks and Tools

- **Bootstrap**: The foundation of Alchemy Aleworks' responsive layout is built on Bootstrap, ensuring consistency and compatibility across various devices. The framework's pre-designed components are customised to align with the brand's unique style and functionality requirements.
- **Custom CSS**: Custom CSS is extensively used to enhance the design, ensuring that specific elements match the project's branding and visual identity.
- **JavaScript**: JavaScript is used for various interactive features, including an age verification modal that uses functional cookies. Other scripts enhance user interaction and streamline the browsing experience.

### Image Sources

- **Unsplash**: High-quality images featured throughout the website are sourced from Unsplash. These images contribute to the overall aesthetic and ambiance of the site.
- **Canva**: Beer labels are designed using Canva, a versatile design tool that allows for the creation of professional and visually appealing labels.
- **Smartmockups**: Beer product mockups are created using Smartmockups, providing realistic and high-quality representations of our products.

### Logo Design

- **Logo.com**: The distinctive logo for Alchemy Aleworks, as well as apparel images, are created using Logo.com. This user-friendly platform ensures that our branding is professional and consistent.

### Favicon Creation

- **Favicon.io**: Custom favicons are generated using Favicon.io, a tool that simplifies the process of creating small, iconic images displayed in web browser tabs. These favicons provide a cohesive branding experience and enhance the website's visual identity.

# Technology Stack

### Backend Framework
**Django**: Utilized for its robust and scalable architecture, Django handles the server-side logic, data processing, and API management, ensuring a secure and efficient backend operation.

### Frontend Framework
**Bootstrap**: Employed for its responsive design capabilities and pre-styled components, Bootstrap ensures a consistent and visually appealing user interface across different devices and screen sizes.
**JQuery**: Included for simplifying HTML document traversing, event handling, and animating, JQuery enhances the interactivity and responsiveness of the user interface.

### Database Management
**Code Institute's Database Maker**: This tool streamlined database management by providing an easy interface for users to input their email addresses and receive a new Postgres database URL. It simplified the process of accessing and managing the project's database, enhancing efficiency and convenience for developers.

### Cloud Storage
**S3**: Amazon S3 is used for storing static and media files, ensuring high availability, durability, and scalability.

### Authentication and Authorisation
**Django AllAuth**: Implemented for user authentication and authorisation, Django AllAuth provides a comprehensive solution for handling user registration, login, logout, and account management.

### Payment Processing
**Stripe**: Used for handling secure and reliable payment processing, ensuring smooth financial transactions on the platform.

### Email Marketing
**MailChimp**: Integrated for managing email marketing campaigns and newsletters, allowing effective communication with users.

### Form Management
**Django Crispy Forms**: Utilized for improving the styling and layout of Django forms, enhancing the user experience when interacting with forms on the site.

### Geolocation Services
**Google Maps API**: Incorporated to provide geolocation services, enabling users to find the brewery location and get directions easily.

### Development Environment
**IDE GitPod**: Used for its cloud-based development environment, GitPod provides an efficient and collaborative space for writing, running, and debugging code.

### Deployment Platform
**Heroku**: Heroku serves as the deployment platform for hosting the live application, providing a reliable and scalable environment that ensures the site is accessible to users. Its seamless integration with Django simplifies the deployment process and allows for efficient management of the application.

### Additional Libraries
**Django Countries**: Provides a database of country names and codes for use in forms and models, enhancing form accuracy and usability.

# Data Models

The data models for Alchemy Aleworks are designed to efficiently manage and represent the core aspects of the brewery's operations and offerings. These models ensure that data is stored in a structured and meaningful way, facilitating smooth interactions and transactions on the website.

Below is an Entity Relationship Diagram create for this project:

![Entity Relationship Diagram](../alchemy-aleworks/static/images/readme/erd.png)

## Inventory

### Beer

The `Beer` model contains detailed information about each beer available for purchase. This includes attributes such as the beer name, type, limited edition boolean, description, alcohol content (ABV), price, and available image.

![Beer Model ERD](../alchemy-aleworks/static/images/readme/beer-erd.png)

### MerchItem

The `MerchItem` model represents the various merchandise products offered by Alchemy Aleworks, such as drinkware, apparel and accessories. This model includes attributes like product name, category, description, sized item boolean, price and image helping to organise the merchandise inventory.

![MerchItem Model ERD](../alchemy-aleworks/static/images/readme/merchitem-erd.png)

## Checkout

### Order

The `Order` model keeps track of customer orders. It includes customer details, order date, delivery fee, order total and grand total amount. This model links to the `CustomerProfile` model to allow autofilling of delivery information if the customer has chosen to save their details.

![Order Model ERD](../alchemy-aleworks/static/images/readme/order-erd.png)

### BeerLineItem

The `BeerLineItem` model represents the specific beers within an order, capturing details such as quantity and price. This model is also linked to both the `Order` and `Beer` models. This model is essential for itemising beer purchases in customer orders.

![BeerLineItem Model ERD](../alchemy-aleworks/static/images/readme/beerlineitem-erd.png)

### MerchLineItem

Similar to the `BeerLineItem`, the `MerchLineItem` model itemises the merchandise products within an order. It includes size, quantity and price. This model is also linked to both the `Order` and `MerchItem` models. Again, similar to the `BeerLineItem` model, this model is essential for itemising merchandise purchases in customer orders.

![MerchLineItem Model ERD](../alchemy-aleworks/static/images/readme/merchlineitem-erd.png)

## Profiles

### CustomerProfile

The `CustomerProfile` model contains information about customers delivery information. This model supports streamlined checkouts and enhanced customer service.

![CustomerProfile Model ERD](../alchemy-aleworks/static/images/readme/customerprofile-erd.png)

# Testing

## User Stories Testing

The table below summarises the testing of user stories, comparing the expected outcomes with the actual outcomes.

| User Story | Expected Outcome | Actual Outcome |
|-|-|-|
| Admin can add a new beer | Admin should be able to successfully add a new beer. | Admin successfully adds a new beer. |
| Admin can update an existing beer | Admin should be able to successfully update the details of an existing beer. | Admin successfully updates an existing beer. |
| Admin can delete a beer | Admin should be able to successfully delete a beer from the website. | Admin successfully deletes a beer. |
| Admin can add a new merchandise item | Admin should be able to successfully add a new merchandise item. | Admin successfully adds a new merchandise item. |
| Admin can update an existing merchandise item | Admin should be able to successfully update the details of an existing merchandise item. | Admin successfully updates an existing merchandise item. |
| Admin can delete a merchandise item | Admin should be able to successfully delete a merchandise item from the website. | Admin successfully deletes a merchandise item. |
| User can view a list of available beers | User should see a list of available beers displayed on the page. | Beer list displays correctly as expected. |
| User can view a list of available merchandise | User should see a list of available merchandise displayed on the page. | Merchandise list displays correctly as expected. |
| User can view detailed information about each beer | User should be able to view detailed information about a selected beer. | Beer detail page shows accurate information. |
| User can view detailed information about each merchandise item | User should be able to view detailed information about a selected merchandise item. | Merchandise detail page shows accurate information. |
| User can easily identify any deals, limited edition releases, or special offers | User should easily identify any deals or special offers prominently displayed. | Deals and special offers are clearly visible as expected. |
| User can learn more about the brewery's story and values | User should have access to information about the brewery's history and values. | Brewery's story and values are well-documented and accessible. |
| User can find information about the taproom | User should easily find information about the brewery's taproom. | Taproom information is easily accessible as expected. |
| User can easily log in or log out of my account | User should be able to log in or log out of their account effortlessly. | Login and logout functionality works smoothly. |
| User can easily register for an account | User should be able to register for a new account without difficulty. | Registration process is straightforward and successful. |
| User can subscribe to the brewery's newsletter | User should be able to subscribe to the brewery's newsletter. | Newsletter subscription functionality works as expected. |
| User can sort the list of available beers | User should be able to sort the list of beers by different criteria. | Beer list can be sorted by criteria like name, ABV, etc. |
| User can sort the list of available merchandise | User should be able to sort the list of merchandise by different criteria. | Merchandise list can be sorted by criteria like name, price, etc. |
| User can search for specific beers or merchandise items by name or description | User should be able to search for items using keywords in the search bar. | Search functionality accurately retrieves items by name or description. |
| Customer can add items to my cart and proceed to checkout seamlessly | Customer should be able to add items to the cart and smoothly proceed to checkout. | Adding items to the cart and checkout process are seamless. |
| Customer can have a smooth and secure checkout process | Customer should experience a secure and hassle-free checkout process. | Checkout process is secure and without issues. |
| Customer can easily select the quantity of a beer or merchandise item when making a purchase | Customer should be able to adjust quantities of items in the cart easily. | Quantity selection in the cart works as intended. |
| Customer can view my cart total and shipping costs before proceeding to checkout | Customer should see a clear breakdown of total cost including shipping. | Cart displays total cost and shipping accurately. |
| Customer can receive order confirmation after completing my purchase | Customer should receive confirmation of their order after completing the purchase. | Order confirmation is sent promptly upon purchase completion. |
| Visitor can access the terms and conditions page | Visitor should be able to access the terms and conditions of using the website. | Terms and conditions page is accessible. |
| Visitor can access the Returns and Delivery procedures page | Visitor should find information on returns and delivery procedures easily. | Returns and delivery procedures are clearly outlined. |
| Visitor can access the privacy policy page | Visitor should be able to access the privacy policy of the website. | Privacy policy page is accessible.

## Unit Tests

## Debugging and Issue Resolution

### Bug Fixes
- **Images not adding to products added through product management**
    - Fixed typos from `item.image.url` to `item.image_url`.

- **Webhook not working when user is logged in**
    - Corrected a typo in the code block that retrieves the customer's username.

- **Spinner overlay not working due to jQuery fadeToggle() function not recognised**
    - Changed to uncompressed jQuery CDN.

- **Stripe elements not showing on HTML template**
    - Wrapped stripe_element.js content within `document.addEventListener('DOMContentLoaded', function() {})` to ensure the page content is loaded beforehand.

- **Error occurs when updating quantity and leaving the box blank in bag and detail pages**
    - Implemented ValidationError logic.

- **Messages do not show for adding an item to the bag that is the same item as an item that is already in the bag**
    - Updated the template logic for displaying messages to show messages depending on their respective levels.

- **Sized items do not allow updating quantities from within the shopping bag**
    - Identified `item_types` from within contexts.py and passed `item_type` when updating quantities.

- **Items with sizes not storing size attribute correctly**
    - Moved `{% if sized_item %}` logic inside the form with add to bag action.

- **Both beer and merch items share the same ID numbers, causing navigation issues**
    - Added a simple adjustment to the URL pattern to include the appropriate 'beers/' or 'merch/' prefix.

- **Overlapping IDs for beer and merch items issue in bag content**
    - Changed product primary key ID values so that beers start at 1001 and merch at 2001. Added functionality to determine product type when adding items to the bag.

- **random_beer and random_merch not showing in bag.html templates**
    - Provided `random_beer` and `random_merch` as single objects using `random_beer[0]` and `random_merch[0]`.

- **Sorting reverts back to all beers rather than the selected category**
    - Preserved the `limited_edition` parameter as a hidden input within the sorting form and passed the `limited_edition` parameter as context in the beers view.

- **Sorting reverts back to all merch rather than the selected category**
    - Preserved the `category` parameter as a hidden input within the sorting form and passed the `category` parameter as context in the merch view.

- **Ensure that the current product does not display within the 'you may also like' suggestions when on the product detail page**
    - Added `exclude_id` to an optional conditional statement within the `get_random_beers` class method to optionally exclude the current `beer_id` passed to the view.

### Known Remaining Bugs
- **Success message displays when a merch item is delete, but not when a beer is deleted even though they are both coded identically.**

## Code Validator Checks

### HTML

The validation checks for HTML markup were performed using the W3C Markup Validation Service. This service ensures that all HTML code adheres to the standards set by the World Wide Web Consortium (W3C), identifying any syntax errors, deprecated elements, or structural issues that could impact the rendering or functionality of the web pages.

#### Home Page

![Home Page HTML Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/home.png)

#### Beers Page

![Beers Page HTML Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/beers.png)

#### Beer Detail Page

![Beer Detail Page HTML Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/beer-detail.png)

#### Merch Page

![Merch Page HTML Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/merch.png)

#### Merch Detail Page

![Merch Detail Page HTML Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/merch-detail.png)

#### Taproom Page

![Taproom Page HTML Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/taproom.png)

#### About Page

![About Page HTML Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/about.png)

#### Add Beer Page

![Add Beer Page HTML Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/add-beer.png)

#### Add Merch Page

![Add Merch Page HTML Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/add-merch.png)

#### Bag Page

![Bag Page HTML Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/bag.png)

#### Checkout Page

![Checkout Page HTML Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/checkout.png)

Note: The validation warning about an empty header element on the Checkout page is false as the header element contains an icon.

#### Checkout Success Page

![Checkout Success Page HTML Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/checkout-success.png)

#### Profile Page

![Profile Page HTML Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/profile.png)

#### Orders and Returns Page

![Orders and Returns Page HTML Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/orders-and-returns.png)

#### Privacy Policy Page

![Privacy Policy Page HTML Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/privacy-policy.png)

#### Terms and Conditions Page

![Terms and Conditions Page HTML Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/terms-and-conditions.png)

### CSS

The CSS files in this project underwent validation using the W3C CSS Validation Service. This service verifies the validity of CSS code according to the CSS specifications outlined by W3C. It ensures that stylesheets are correctly written, free of syntax errors, and adhere to the standards, promoting consistency and compatibility across different browsers.

#### base.css

![base.css Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/base-css.png)

#### inventory.css

![inventory.css Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/inventory-css.png)

#### checkout.css

![checkout.css Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/checkout-css.png)

#### profile.css

![profile.css Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/profile-css.png)

### JavaScript

For JavaScript code quality assurance, JSHint was used to perform validation checks. JSHint analyses JavaScript code for potential errors, coding conventions, and stylistic inconsistencies. It helps ensure that the JavaScript code is clean, efficient, and follows best practices, thereby enhancing readability and maintainability.

#### age_verification_modal.js

![Age Verification Modal Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/age-verification-modal.png)

#### country_field.js

![Country Field Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/country-field.png)

**Note:** All warnings shown relate to complaints about ES6 syntax.

#### custom_validate_email.js

![Custom Validate Email Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/custom-validate-email.png)

#### scroll_position.js

![Scroll Position Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/scroll-position.png)

**Note:** All warnings shown relate to complaints about ES6 syntax.

#### stripe_elements.js

![Stripe Elements Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/stripe-elements.png)

**Note:** The undefined variable flagged is due to Stripe being initialised as an environment variable within the environment configuration files rather than directly in the JavaScript code. Additional warnings shown relate to complaints about ES6 syntax.

#### age_verification_modal.js

![Age Verification Modal Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/age-verification-modal.png)

#### Additional Script Tags

![Additional Script Tags Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/additional-script-tags.png)

**Note:** All warnings shown pertain exclusively to the MailChimp script.

### Python

Validation of Python code was conducted using Code Institute's Python Linter. This tool ensures adherence to Python coding standards and best practices, highlighting any syntax errors, style violations, or potential pitfalls in the code. By using this linter, the Python code is validated to be structured correctly, enhancing readability and maintainability throughout the development process.

#### Alchemy Aleworks Main Project Folder

#### settings.py

![Alchemy Aleworks settings.py Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/alchemy-aleworks/settings.png)

**Note:** 4 validator errors appear due to AllAuth password validator variables being significantly long.

#### urls.py

![Alchemy Aleworks urls.py Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/alchemy-aleworks/urls.png)

#### views.py

![Alchemy Aleworks views.py Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/alchemy-aleworks/views.png)

#### Bag App

#### bag_tools.py

![Bag bag_tools.py Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/bag/bag-tools.png)

#### contexts.py

![Bag contexts.py Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/bag/contexts.png)

#### urls.py

![Bag urls.py Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/bag/urls.png)

#### views.py

![Bag views.py Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/bag/views.png)

#### Checkout App

#### admin.py

![Checkout admin.py Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/checkout/admin.png)

#### apps.py

![Checkout apps.py Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/checkout/apps.png)

#### forms.py

![Checkout forms.py Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/checkout/forms.png)

#### models.py

![Checkout models.py Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/checkout/models.png)

#### signals.py

![Checkout signals.py Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/checkout/signals.png)

#### urls.py

![Checkout urls.py Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/checkout/urls.png)

#### views.py

![Checkout views.py Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/checkout/views.png)

#### webhook_handler.py

![Checkout webhook_handler.py Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/checkout/webhook-handler.png)

**Note:** This warning is caused by the use of `iexact` lookup variables in Django queries. The `iexact` lookups are essential for case-insensitive exact matches and ensure the proper functioning of the queries. Reducing the length of these lines is not feasible without compromising readability and functionality.

#### webhooks.py

![Checkout webhooks.py Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/checkout/webhooks.png)

#### Home App

#### urls.py

![Home urls.py Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/home/urls.png)

#### views.py

![Home views.py Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/home/views.png)

#### Inventory App

#### admin.py

![Inventory admin.py Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/inventory/admin.png)

#### forms.py

![Inventory forms.py Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/inventory/forms.png)

#### models.py

![Inventory models.py Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/inventory/models.png)

#### urls.py

![Inventory urls.py Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/inventory/urls.png)

#### views.py

![Inventory views.py Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/inventory/views.png)

#### Pages App

#### urls.py

![Pages urls.py Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/pages/urls.png)

#### views.py

![Pages views.py Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/pages/views.png)

#### Profiles App

#### forms.py

![Profiles forms.py Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/profiles/forms.png)

#### models.py

![Profiles models.py Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/profiles/models.png)

#### urls.py

![Profiles urls.py Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/profiles/urls.png)

#### views.py

![Profiles views.py Validator Results](../alchemy-aleworks/static/images/readme/validator-checks/profiles/views.png)

## Lighthouse

During testing, it was noted that the best practices score was impacted by the fact that the application uses third-party cookies from Stripe and MailChimp. These are essential for specific functionalities such as payment processing and marketing tools. While developer tools like Lighthouse may flag these cookies, it's important to understand that they are integral to the core features and operations of the project.

#### Home Page

![Home Page Lighthouse Results](../alchemy-aleworks/static/images/readme/lighthouse/home.png)

#### Beers Page

![Beers Page Lighthouse Results](../alchemy-aleworks/static/images/readme/lighthouse/beers.png)

#### Beer Detail Page

![Beer Detail Page Lighthouse Results](../alchemy-aleworks/static/images/readme/lighthouse/beer-detail.png)

#### Merch Page

![Merch Page Lighthouse Results](../alchemy-aleworks/static/images/readme/lighthouse/merch.png)

#### Merch Detail Page

![Merch Detail Page Lighthouse Results](../alchemy-aleworks/static/images/readme/lighthouse/merch-detail.png)

#### Taproom Page

![Taproom Page Lighthouse Results](../alchemy-aleworks/static/images/readme/lighthouse/taproom.png)

#### About Page

![About Page Lighthouse Results](../alchemy-aleworks/static/images/readme/lighthouse/about.png)

#### Add Beer Page

![Add Beer Page Lighthouse Results](../alchemy-aleworks/static/images/readme/lighthouse/add-beer.png)

#### Add Merch Page

![Add Merch Page Lighthouse Results](../alchemy-aleworks/static/images/readme/lighthouse/add-merch.png)

#### Bag Page

![Bag Page Lighthouse Results](../alchemy-aleworks/static/images/readme/lighthouse/bag.png)

#### Checkout Page

![Checkout Page Lighthouse Results](../alchemy-aleworks/static/images/readme/lighthouse/checkout.png)

**Note:** The lower accessibility score on this page is primarily influenced by the presence of Stripe payment processing elements `.__PrivateStripeElement-input`. These elements are essential for secure payment handling but may impact accessibility scores due to their interaction within the page structure.

#### Checkout Success Page

![Checkout Success Page Lighthouse Results](../alchemy-aleworks/static/images/readme/lighthouse/checkout-success.png)

#### Profile Page

![Profile Page Lighthouse Results](../alchemy-aleworks/static/images/readme/lighthouse/profile.png)

**Note:** Select elements in our forms are rendered using Django Crispy Forms, which may lack explicit `<label>` elements but are programmatically associated with their corresponding form fields through attributes like `for` and `id`, ensuring accessibility to screen readers.

#### Orders and Returns Page

![Orders and Returns Page Lighthouse Results](../alchemy-aleworks/static/images/readme/lighthouse/orders-and-returns.png)

#### Privacy Policy Page

![Privacy Policy Page Lighthouse Results](../alchemy-aleworks/static/images/readme/lighthouse/privacy-policy.png)

#### Terms and Conditions Page

![Terms and Conditions Page Lighthouse Results](../alchemy-aleworks/static/images/readme/lighthouse/terms-and-conditions.png)

# Deployment

# Credits