function [L]=calculdL(T1,T2,l0,alpha)

#convertion of your entries into Kelvin degrees and meters.
t2 = T2 + 273.15;
L0 = l0 *10^(-3);


L = L0*(1+ alpha * (t2 - T1 ) )
endfunction