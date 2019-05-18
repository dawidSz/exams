Projekt majêcy na celu zapewnienie mo¿liwoœci wy³uskania danych na temat wyników matur na przestrzeni lat 2010-2018.

Projekt jest typow¹ pythonow¹ paczk¹, dlatego te¿ polecam j¹ pobraæ i w Pycharmie otworzyæ 
mojego mastera: exams-master. Nastepnie wystarczy jedynie dodaæ konfiguracjê uruchamiaj¹c¹ pod modu³ examsdata,
wybraæ swój interpreter i voila!
Wa¿n¹ kwesti¹ jest równie¿ ustalenie kodowania znaków na UTF-8.
Ja tworzy³em projekt w venv'ie by dzia³aæ na pustym interpreterze, jedynie z domyœlnymi modu³ami,
lecz nie powinno byæ niekompatybilnoœci je¿eli ktoœ u¿yje swojego. Iloœæ u¿ywanych przeze mnie modu³ów jest b¹dŸ co b¹dŸ znikoma.

Trochê obs³ugi: 
		Prim. Na pocz¹tku ukazuje siê menu, gdzie wpisuj¹c za s³owem 'opcja >>' numer interesuj¹cego nas
		polecenia wybieramy to co chcemy zrobiæ. 
		1. Gdy wybierzemy jedynkê, mo¿emy sprawdziæ œredni¹ zdawalnoœæ na województwo danego rocznika.
			Komendy przyjmowane w tym przypadku to np.: '2018 kobiety', '2010 mê¿czyŸni', '2011'
			Oczywiœcie brak okreœlenia p³ci zapewnia rozpatrywanie denych bez wzglêdu na ni¹.
		2. Wybieraj¹c drug¹ opcjê nale¿y podaæ jedynie poprawn¹ nazwê województwa. Tutaj równie¿ mo¿emy opcjonalnie podaæ p³eæ.
			('lubuskie', 'lubuskie kobiety', 'lubuskie mê¿czyŸni')
		3. Analogicznie w tym punkcie podajemy rok i p³eæ, lub jej brak. Np.: '2018 kobiety', '2010'
		4. Wybieraj¹c opcjê 4 mo¿my wpisaæ s³owo klucz 'kobiety', 'mê¿czyŸni' lub po prostu nie wpisywaæ nic i klikn¹æ Enter.
		5. Z kolei tutaj wystarczy podaæ dwie nazwy woj. > 'lubuskie œl¹skie kobiety' (opcjonalnie p³eæ)
	
Widaæ zatem, ¿e obs³uga programu jest dosyæ prosta. 