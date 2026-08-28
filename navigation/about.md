---
layout: post
title: About Me!
permalink: /about/
comments: true
---

<link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700&display=swap" rel="stylesheet">
<style>
    .post-content {
        font-family: 'Merriweather', serif;
    }
</style>

## As a conversation Starter

Here are some places I have lived at:

<comment>
Flags are made using Wikipedia images
</comment>

<style>
    /* Style looks pretty compact, 
       - grid-container and grid-item are referenced the code 
    */
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); /* Dynamic columns */
        gap: 10px;
    }
    .grid-item {
        text-align: center;
    }
    .grid-item img {
        width: 100%;
        height: 100px; /* Fixed height for uniformity */
        object-fit: contain; /* Ensure the image fits within the fixed height */
    }
    .grid-item p {
        margin: 5px 0; /* Add some margin for spacing */
    }

</style>

<!-- This grid_container class is used by CSS styling and the id is used by JavaScript connection -->
<div class="grid-container" id="grid_container">
    <!-- content will be added here by JavaScript -->
</div>

<script>
    // 1. Make a connection to the HTML container defined in the HTML div
    var container = document.getElementById("grid_container"); // This container connects to the HTML div

    // 2. Define a JavaScript object for our http source and our data rows for the Living in the World grid
    var http_source = "https://upload.wikimedia.org/wikipedia/commons/";
    var living_in_the_world = [
        {"flag": "0/01/Flag_of_California.svg", "greeting": "Hey", "description": "California - 5 years"},
        {"flag": "b/b5/Flag_of_Michigan.svg", "greeting": "Hello", "description": "Michigan - 5 and a half years"},
        {"flag": "4/41/Flag_of_India.svg", "greeting": "Namaste", "description": "India - 2 years"},
    ];

    // 3a. Consider how to update style count for size of container
    // The grid-template-columns has been defined as dynamic with auto-fill and minmax

    // 3b. Build grid items inside of our container for each row of data
    for (const location of living_in_the_world) {
        // Create a "div" with "class grid-item" for each row
        var gridItem = document.createElement("div");
        gridItem.className = "grid-item";  // This class name connects the gridItem to the CSS style elements
        // Add "img" HTML tag for the flag
        var img = document.createElement("img");
        img.src = http_source + location.flag; // concatenate the source and flag
        img.alt = location.flag + " Flag"; // add alt text for accessibility

        // Add "p" HTML tag for the description
        var description = document.createElement("p");
        description.textContent = location.description; // extract the description

        // Add "p" HTML tag for the greeting
        var greeting = document.createElement("p");
        greeting.textContent = location.greeting;  // extract the greeting

        // Append img and p HTML tags to the grid item DIV
        gridItem.appendChild(img);
        gridItem.appendChild(description);
        gridItem.appendChild(greeting);

        // Append the grid item DIV to the container DIV
        container.appendChild(gridItem);
    }
</script>

### Journey through Life

Here is a timeline of my life!

- 🏫 Preschool and Elementary School in San Diego CA at Ericson Elementary School
- 🏫 Elementary and Upper Elementary School in Novi MI at Parkview Elementary School and Novi Meadows Upper Elementary
- 🏫 Middle School in Torrance CA at Jefferson Middle School
- 🏫 Half of high school(freshman and sophmore year) at Rockwell International School in Hyderabad, India
- 🏫 Currently finishing high school(junior year) at Del Norte High School in San Diego CA 


### Places I Traveled

Here are some of my favorite places I have traveled to!

- ✈️ Hawaii!
- ✈️ Las Vegas
- ✈️ White Pockets
- ✈️ Death Valley
- ✈️ Horseshoe Bend
- ✈️ Antelope Canyon
- And so many more!

All of these pictures were taken by me!

<style>
    .travel-gallery {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
    }
    .travel-gallery figure {
        margin: 0;
        width: 200px;
    }
    .travel-gallery img {
        width: 100%;
        height: 150px;
        object-fit: cover;
        border-radius: 5px;
    }
    .travel-gallery figcaption {
        font-size: 0.85em;
        color: gray;
        text-align: center;
        margin-top: 5px;
    }
    .travel-gallery img.crop-top {
        object-position: top;
    }
    .travel-gallery img.crop-formation {
        object-position: center 60%;
    }
    .travel-gallery .rotate-wrap {
        position: relative;
        width: 100%;
        height: 150px;
        overflow: hidden;
        border-radius: 5px;
    }
    .travel-gallery .rotate-wrap img {
        position: absolute;
        top: 50%;
        left: 50%;
        width: 150px;
        height: 200px;
        transform: translate(-50%, -50%) rotate(-90deg);
    }
</style>

<div class="travel-gallery">
  <figure>
    <img src="{{site.baseurl}}/images/about/hawaii.jpeg" alt="Hawaii">
    <figcaption>Hawaii!</figcaption>
  </figure>
  <figure>
    <div class="rotate-wrap">
      <img src="{{site.baseurl}}/images/about/vegas.jpeg" alt="Las Vegas">
    </div>
    <figcaption>Las Vegas</figcaption>
  </figure>
  <figure>
    <img class="crop-formation" src="{{site.baseurl}}/images/about/whitepockets.jpeg" alt="White Pockets">
    <figcaption>White Pockets</figcaption>
  </figure>
  <figure>
    <img class="crop-top" src="{{site.baseurl}}/images/about/death_valley.jpeg" alt="Death Valley">
    <figcaption>Death Valley</figcaption>
  </figure>
  <figure>
    <img class="crop-top" src="{{site.baseurl}}/images/about/horseshoe_bend.jpeg" alt="Horseshoe Bend">
    <figcaption>Horseshoe Bend</figcaption>
  </figure>
  <figure>
    <img class="crop-top" src="{{site.baseurl}}/images/about/antelope_canyon.jpeg" alt="Antelope Canyon">
    <figcaption>Antelope Canyon</figcaption>
  </figure>
</div>


### Family and Friends!

Most of my best memories were made with my family and my best friends!
There's nothing I value more than friends and a good relationship with your family
- My family is pretty small, just my parents, my brother, and I. The rest of our family lives in India, but the people I've always connected to most were my grandparents on my mother's side, my uncle on my mother's side, and my cousins on both sides! 
- Growing up, I've always moved around a lot. In fact, this year is my 5th time moving to another place. 
Luckily, I've always managed to make friends everywhere I went. Whether I was happy or sad, I could always count on my friends to be there for me. 
Some friends I connected to more than most. I've been maintaining these friendships for many years thousands of miles away. 

Here is a gallery of photos showcasing some of the memories I made with my friends and family!

<style>
    .photo-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 12px;
    }
    .photo-grid .cell {
        aspect-ratio: 1 / 1;
        background: #ffffff;
        border-radius: 10px;
        box-shadow: 0 1px 4px rgba(0, 0, 0, 0.12);
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
    }
    .photo-grid img {
        max-width: 100%;
        max-height: 100%;
        object-fit: contain;
    }
    .photo-grid img.turn {
        transform: rotate(-90deg);
    }
    @media (max-width: 480px) {
        .photo-grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }
</style>

<comment>
Gallery of Pics:
</comment>
<div class="photo-grid">
  <div class="cell"><img src="{{site.baseurl}}/images/about/family.jpg" alt="Family"></div>
  <div class="cell"><img src="{{site.baseurl}}/images/about/brother.jpg" alt="Brother"></div>
  <div class="cell"><img src="{{site.baseurl}}/images/about/friends1.jpg" alt="Friends"></div>
  <div class="cell"><img src="{{site.baseurl}}/images/about/friends2.jpg" alt="Friends"></div>
  <div class="cell"><img class="turn" src="{{site.baseurl}}/images/about/friends3.jpg" alt="Friends"></div>
  <div class="cell"><img src="{{site.baseurl}}/images/about/friends4.jpg" alt="Friends"></div>
  <div class="cell"><img class="turn" src="{{site.baseurl}}/images/about/friends5.jpg" alt="Friends"></div>
  <div class="cell"><img class="turn" src="{{site.baseurl}}/images/about/friends6.jpg" alt="Friends"></div>
</div>
