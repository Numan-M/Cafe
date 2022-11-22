<a name="readme-top"></a>
# CLI Application for a Café
A CLI program able to view, add, rename and delete products, couriers, orders from a list of dictionaries persisting the stored data. 

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#Design Choices">Design Choices</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
This CLI project began my journey of programming from a beginner level, polishing my skills along the way, getting a good grasp of the basics of Python and most importantly shining a light on unit testing a concept that was very new to me but made complete sense when brought to my attention. 

### Design Choices
My approach to this project took strong inspiration from the term clean code, I did everything in my effort to avoid "redundant code" whilst ensuring idempotency was achieved in all aspects. Following the user's input, a set of simple menus appear similar in functionality and appearance forming the backbone of the application. Effortless transition can be made to and from these menus with respect to the users commands. Alteration of the specs of the code on a weekly basis, imitated the working environment of collaborating with clients which brought about feelings of uncertainty as to how the final product would turn out. Many times of the course of the 6 weeks, time spent on implementing ideas were removed in their entirety however, the skills learned from the initial implentation were retained. In addition to learning new programming skills, certain practices were also acquired through refactoring and simplifying code.

# Areas to Improve.
With more time I'd like to implement week 5 and 6 of the clients spec but, with the current iteration of the program it would greatly benefit from implementing try-except blocks for when the user is asked to enter a value requiring a certain datatype.


<!-- GETTING STARTED -->
## Getting Started

 ### Installation

1. Clone the repo
   ```sh
   git clone git@github.com:Numan-M/Cafe.git
   ```
2. Create a virtual environment
   ```sh
   python3 -m venv venv
   source ./venv/bin/activate
   ```
3. Install dependencies
  ```sh
  pip install -r requirements.txt
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage
### Main Menu
![image](https://user-images.githubusercontent.com/115251414/203418269-601dfef1-4be0-4fd1-9f13-021d1a7ad781.png)

### Products Menu
![image](https://user-images.githubusercontent.com/115251414/203418410-616d444c-f58c-4405-aa9b-1c600fe24149.png)

* 1. Display

![image](https://user-images.githubusercontent.com/115251414/203418465-5c8b4c04-32f9-45d4-821c-f367f54670ea.png)

* 2. Add

![image](https://user-images.githubusercontent.com/115251414/203420935-ac52e54a-4439-4670-97f4-861ff49c702c.png)

* 3. Rename

![image](https://user-images.githubusercontent.com/115251414/203421085-40872e1c-721a-4510-bd81-3c342d3e0275.png)

* 4. Remove

![image](https://user-images.githubusercontent.com/115251414/203421143-7c005856-c40e-4ff3-b3a7-390dc7eec6cf.png)

### Couriers Menu

![image](https://user-images.githubusercontent.com/115251414/203421616-2f5214f4-9210-4f5d-94eb-9ae7d77b9609.png)

* 1. Display

![image](https://user-images.githubusercontent.com/115251414/203421662-892b263f-04ea-4af8-ab03-04dfeca51396.png)

* 2. Add

![image](https://user-images.githubusercontent.com/115251414/203421852-fd4ad7a0-f466-4587-81be-ec83d41e3b5c.png)

* 3. Rename

![image](https://user-images.githubusercontent.com/115251414/203421960-3494243e-1a85-4ada-9889-db65aca810d4.png)
![image](https://user-images.githubusercontent.com/115251414/203421984-527c9d9e-f5cf-4318-96bc-78a87b04b22f.png)

* 4. Remove

![image](https://user-images.githubusercontent.com/115251414/203422028-e304291a-ed47-4c97-a9ad-f81c8124474f.png)

### Orders Menu

![image](https://user-images.githubusercontent.com/115251414/203422083-23afa487-ab64-42a5-92bf-2e40613f58f2.png)

* 1. Display

![image](https://user-images.githubusercontent.com/115251414/203422226-d1e933bc-8d5c-41df-995e-1b8e382c377c.png)

* 2. Add

![image](https://user-images.githubusercontent.com/115251414/203422779-9cc04f1b-4fb4-4bcf-8e8b-e39b6657d290.png)

![image](https://user-images.githubusercontent.com/115251414/203422880-d0039dad-544a-42da-80ca-1aeb73453715.png)


* 3. Update status

![image](https://user-images.githubusercontent.com/115251414/203423253-ca5e7e4d-3e1e-4ff6-8d57-fc4032c55872.png)

* 4. Update all

![image](https://user-images.githubusercontent.com/115251414/203424212-5fa5958b-eb0d-4f03-9a32-481b285c2c68.png)

* 5. Cancel 

![image](https://user-images.githubusercontent.com/115251414/203424291-47bc22ed-b1ac-499b-8df5-8aa5b264c420.png)


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [ ] Week 1
  ``` 
  As a user I want to:
  create a product and add it to a list
  view all products
  STRETCH update or delete a product
  ```

- [ ] Week 2
  ```
  As a user I want to:
  create a product or order and add it to a list
  view all products or orders
  STRETCH I want to be able to update or delete a product or orde
  ```
  
- [ ] Week 3
  ```
  As a user I want to:
  create a product, courier, or order and add it to a list
  view all products, couriers, or orders
  update the status of an order
  persist my data (products and couriers)
  STRETCH update or delete a product, order, or courier
  ```
  
- [ ] Week 4
  ```
  To show that our code works, we will also need to write unit tests to prove that
  our app works correctly.
  
  As a user I want to:
  create a product, courier, or order dictionary and add it to a list
  view all products, couriers, or orders
  update the status of an order
  persist my data
  STRETCH update or delete a product, order, or courier
  BONUS list orders by status or courier
  ```




<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Numan Mahmood - [LinkedIn](https://www.linkedin.com/in/numan-mahmood-197951242/) - Numan_Mahmood@hotmail.co.uk

Project Link: [https://github.com/Numan-M/Cafe](https://github.com/Numan-M/Cafe)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Patrick Cando
* Carlton Nunes
* Sheikh Osman
* Faaruq M.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

