Projekt maj�cy na celu zapewnienie mo�liwo�ci wy�uskania danych na temat wynik�w matur na przestrzeni lat 2010-2018.

Projekt jest typow� pythonow� paczk�, dlatego te� polecam j� pobra� i w Pycharmie otworzy� 
mojego mastera: exams-master. Nastepnie wystarczy jedynie doda� konfiguracj� uruchamiaj�c� pod modu� examsdata,
wybra� sw�j interpreter i voila!
Wa�n� kwesti� jest r�wnie� ustalenie kodowania znak�w na UTF-8.
Ja tworzy�em projekt w venv'ie by dzia�a� na pustym interpreterze, jedynie z domy�lnymi modu�ami,
lecz nie powinno by� niekompatybilno�ci je�eli kto� u�yje swojego. Ilo�� u�ywanych przeze mnie modu��w jest b�d� co b�d� znikoma.

Troch� obs�ugi: 
		Prim. Na pocz�tku ukazuje si� menu, gdzie wpisuj�c za s�owem 'opcja >>' numer interesuj�cego nas
		polecenia wybieramy to co chcemy zrobi�. 
		1. Gdy wybierzemy jedynk�, mo�emy sprawdzi� �redni� zdawalno�� na wojew�dztwo danego rocznika.
			Komendy przyjmowane w tym przypadku to np.: '2018 kobiety', '2010 m�czy�ni', '2011'
			Oczywi�cie brak okre�lenia p�ci zapewnia rozpatrywanie denych bez wzgl�du na ni�.
		2. Wybieraj�c drug� opcj� nale�y poda� jedynie poprawn� nazw� wojew�dztwa. Tutaj r�wnie� mo�emy opcjonalnie poda� p�e�.
			('lubuskie', 'lubuskie kobiety', 'lubuskie m�czy�ni')
		3. Analogicznie w tym punkcie podajemy rok i p�e�, lub jej brak. Np.: '2018 kobiety', '2010'
		4. Wybieraj�c opcj� 4 mo�my wpisa� s�owo klucz 'kobiety', 'm�czy�ni' lub po prostu nie wpisywa� nic i klikn�� Enter.
		5. Z kolei tutaj wystarczy poda� dwie nazwy woj. > 'lubuskie �l�skie kobiety' (opcjonalnie p�e�)
	
Wida� zatem, �e obs�uga programu jest dosy� prosta. 