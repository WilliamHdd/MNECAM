function [L]=calculdL(T1,T2,l0,alpha)
t2 = T2 + 273.15;
L0 = l0 * 1000;
L = L0+ alpha * (t2 - T1 ) 
endfunction