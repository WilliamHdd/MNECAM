#Please enter the start and end temperature in celcius degrees.
T1 = 20;
T2 = 120;

# Please enter the initial length of the object of your choice in milimeters.

lo = 200;

#Please enter the dilatation coefficient of the objet of your choice. This can be find on the internet if you don't know it.
alpha = 1.6;

title('Longueur finale en fonction de la témparature ')
xlabel('Température')
ylabel('Longueur finale')

# The graph you'll get takes the temperature in Kelvin degrees on the X axis, and the lenght of your objet on the Y axis. This length is calculated by the function " calculdL".
x = [T1+273.15:10:T2+273.15];
y = calculdL(T1,x,lo,alpha);

plot(x,y)