# Signum
 Powerful Math module using MPMath
>Делал для себя, тк это удобно.

Это обертка для модуля [mpmath](https://mpmath.org/doc/1.2.0/basics.html)

Который решает проблемы [неточной математики в python](https://stackoverflow.com/questions/10403434/floating-point-in-python-gives-a-wrong-answer)

Изза [двоичного хранения чисел в python](https://docs.python.org/3/tutorial/floatingpoint.html)

# А я тут причём?
От себя я добавил Углы (Signum.Angle)
>Число лежащее всегда между 0 и 360

Векторы (Signum.Vector)
>Их можно легко складывать и вычитать

Проекции этих векторов (Signum.Projection)
>О них ниже

```python
>>> import Signum as m

>>> m.num(10) #Логичный вопрос - а зачем?
mpf(10)

>>> 2.2-1.2
1.0000000000000002 # Тип float python достаточно неточный https://docs.python.org/3/tutorial/floatingpoint.html

>>> m.num("2.2")-m.num("1.2") # И тут та же проблема...
mpf('1.0000000000000002')

>>> m.mp.dps=50 # Увеличим точность математики...
>>> m.num("2.2")-m.num("1.2") # Число стало более точным
mpf('1.0000000000000000000000000000000000000000000000000027')

>>> m.Angle(30) #Это угол, в чем отличие от обычного int?
Angle <30.0°>

>>> m.Angle(365) #Во первых он не бывает >360 или <0
Angle <5.0°>

>>> m.Angle(270)+m.Angle(100) #С ними можно выполнять + и -
Angle <10.0°>

>>> m.Vector(180,5) #Это вектор, т.е. угол+число
Vector <180.0°,5.0>

>>> m.Vector(180,5)+m.Vector(90,5) #Это сложение векторов)
Vector <135.0°,7.07106781186548>

>>> m.Vector(180,10)-m.Vector(180,5) #Или даже вычитание

>>> p=m.Project(5,5) #Это просто пара чисел

>>> p #Но в чем отличие от [5,5] или (5,5)?
Projection <5.0;5.0>

>>> p.from_Vector(m.Vector(90,5)) #Она умеет брать с вектора его компоненты x y
Projection <5.0;0>

>>> m.Project(0,5)+m.Project(10,0) #Их тоже можно сравнивать
Projection <10.0;5.0>

#Так жа реализованы всякие sin cos и тд для более точной математики
```
