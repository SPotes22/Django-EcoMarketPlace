## Market place project with Django
whis prject covers the basics of Django by building a simple online marketplace where people can buy and sell items. this its an exaple on how I implemented:
----
- Authentication 

- Communication between users

- Dashboard for your items

- Form handling and customizations

- and more

# Disclaimer 

this project was made for educational purposes
besed on the explanatios of CodeWithStein on 2023 for FreeCodeCamp.org
https://www.freecodecamp.org
https://twitter.com/codewithstein

thanks a lot to freeCodeCamp to provide such as usefull and dynamic way to learn the current necesities on the industry.

---

# PROYECTO GREENX

	- VIEW TRANSACCIONES 
	- REDIRECIONAMIENTO DISTINTO
	- DB UPDATED
	- PENTESTING
		- SLQI
		- man in the middle

	- INTEGRADO A UNA API
	- CONVERTIDO EN TEMPLATE EXPORTABLE

# USO

- Crear un venv 
`
python3 -m venv env
`
- instalar librerias
`
pip install -r requirements.txt
`
- Conectar BD desde puddle/settings.py
- Crear Usuario y bd del Proyecto
- Preparar Migraciones de los modelos
`
python3 manage.py makemigrations
`
- migrar a la bd 
`
python3 manage.py migrate
`
- crear  admin (opcional)
- activar admin (obligatorio desde db field core_customuser.'is_active' == 1)
- crear usuario 
- activar usuario desde la bd (core_customuser.'is_active'==1)
- ejecutar en DEBUG
`
python3 manage.py runserver
`
- Empezar a editar 


