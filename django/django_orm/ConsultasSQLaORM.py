SQL a ORM
#Para cada una de las siguientes consultas SQL, envíe el comando ORM correspondiente que haría lo mismo.
#Nota: Es posible que deba agregar el nombre de su base de datos para que estas consultas se ejecuten en MySQLWorkbench. es decir, INSERT INTO hogwarts_db.Wizard

INSERT INTO Wizard (name, house, pet, year) VALUES ('Harry Potter', 'Gryffindor', 'Hedwig', '5');
R: 
from hogwartsapp.models import Wizard
Wizard.objects.create(name='Harry Potter', house='Gryffindor', pet='Hedwig', year=5)

INSERT INTO Wizard (name, house, pet, year) VALUES ('Hermione Granger', 'Gryffindor', 'Crookshanks', '5');
R: Wizard.objects.create(name='Hermione Granger', house='Gryffindor', pet='Crookshanks', year=5)

SELECT * FROM Wizard WHERE id = 1;
R: Wizard.objects.get(id=1)

SELECT * FROM Wizard WHERE house = 'Gryffindor';
R: Wizard.objects.filter(house='Gryffindor')

UPDATE Wizard SET year = '6' WHERE id = 1;
R: 
Updatewizard = Wizard.objects.get(id=1)
updatewizard.year = 6
updatewizard.save()


ORM a SQL
#Para cada uno de los siguientes segmentos de comando ORM, envíe la consulta SQL correspondiente que haría lo mismo.

Wizard.objects.create(name="Luna Lovegood", house="Ravenclaw", pet="None", year="4")
R: INSERT INTO Wizard (name, house, pet, year) VALUES ('Luna Lovegood', 'Ravenclaw', 'None', '4');

Wizard.objects.create(name="Padma Patil", house="Ravenclaw", pet="None", year="5")
R: INSERT INTO Wizard (name, house, pet, year) VALUES ('Padma Patil', 'Ravenclaw', 'None', '5');

ravenclaws = Wizard.objects.filter(house="Ravenclaw")
R: SELECT * FROM Wizard WHERE house = 'Ravenclaw';

luna = Wizard.objects.get(name="Luna Lovegood")
luna.year = 5
luna.save()
R: UPDATE Wizard SET year = '5' WHERE name = 'Luna Lovegood';