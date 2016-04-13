T1 = 20;
T2 = 120;
lo = 200;
alpha = 1.6;

x = [T1+273.15:10:T2+273.15];
y = calculdL(T1,x,lo,alpha);

plot(x,y)