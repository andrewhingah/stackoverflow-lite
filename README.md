# stackoverflow-lite
StackOverflow-lite is a platform where people can ask questions and provide answers.
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purpose
## Prerequisites
You need to have the following installed.
- [Git](https://git-scm.com/)
- [Postman](https://www.getpostman.com/)
- [Python 3.6](https://www.python.org/)
- [Pip](https://pypi.org/)
## Installing
1. Clone the repository
```git clone https://github.com/andrewhingah/stackoverflow-lite.git```

2. Change directory
```cd stackoverflow-lite```

3. Checkout to develop branch
```git checkout develop```

4. To view UI designs, navigate to the UI/ directory
```cd UI/```

Open ```index.html``` on your browser

5. To test API locally, set up a virtual environment in the base project folder
```python -m venv venv```

6. Activate the virtual environment
```venv\Scripts\activate```

7. Install dependecies
```pip install -r requirements.txt```

8. Run tests
```pytest``` or ```nosetests --exe --with-coverage --cover-package=api```

9. Test the endpoints on postman

For instance to post a new question you send a request to ```http://127.0.0.1:5000/questions```

A sample post question request should be as shown below

'''{
	"question":"What is an API?"
}'''

## Built with
- Python 3.6
- Flask
- HTML5
- CSS
- JavaScript
## Contributing
1. Fork it from ```https://github.com/andrewhingah/stackoverflow-lite.git/fork```

2. Create your feature branch ```git branch somefeature``` ```git checkout somefeature```

3. Commit your changes ```git commit "Add some feature"```

4. Push to the branch ```git push origin somefeature```

5. Create a new pull request

## Author(s)
Andrew Hinga andrewhinga5@gmail.com
