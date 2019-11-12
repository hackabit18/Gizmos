# CodeOnPaper ![CI status](https://img.shields.io/badge/build-passing-brightgreen.svg)

Learning has no age barriers. The early we start the more time we have to master a particular field of study. The same goes with mastering the art of writing codes. The early we start the better we are at it. But the major problem lies in the availability of resources i.e. basically computers and laptops. A majority of the population does not have access to these facilities. But when compared to having laptops or computers it is quite easy to find smartphones among the majority. But life is not so easy when it comes to code on a smartphone. However, it is much easy to write a code an paper than to write it on a smartphone but how to run and compile this handwritten code? Well, every problem has a solution and so does this. The solution is that we code scan this code and then digitalize it and compile-run it on the cloud. Well, this is basically the underlying idea **CodeOnPaper**.


## Technologies Used

* **Google Vision API**
* **Django**
* **Firebase**

## Installation

### Requirements
* Android KitKat and higher (>4.4)


[Get the app here](https://drive.google.com/open?id=1XwSxOZ09ntXjW8ngqldEI85Z8WpLnH05)


## WorkFlow
* Android App Scans photo of a handwritten piece of code 
* Sends request to DJANGO server that performs OCR (Optical Character Recognition) using Google Vision API 
* Server runs a custom script that detects and corrects syntax errors 
* Final text file is returned to the device for the user to make final changes, compile and run on another API.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## The Team
* [Abhinav Jha](https://github.com/aBITnav)
* [Ali Sabir](https://github.com/sabirali2560)
* [Osama Azmi](https://github.com/Samuelimza)
* [Owais Hasnath Ahmed](https://github.com/owais34)



