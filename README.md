# PyHub


PyHub is a modular __Python-based__ entry point that can run certain feature modules from a central entry point such as games, calculators, and dictionaries.

## Features

<br>

Project Structure

PyHub/

├── features/       
├── dat.py        
├── main.py                   
├── .gitignore                   
├── README.md                    
├── .gitattributes          
└── LICENSE                        


## Contribution

Clone the repository
```bash
git clone https://github.com/gameingame-eng/PyHub.git

cd PyHub
```
Run the project
```bash
python3 main.py
```

### Add your own features

Create a new file inside features/:

__File: features/my_feature.py__
```python
def run():
print("My feature is running!")
```
Then import or register it in main.py..

## Requirements

__Python 3.12.10__

__No__ external dependencies (unless you add them)

**Pull requests are welcome.** For major changes, please __*open an issue*__ first to discuss what you’d like to modify.
