from spm.__wrapper__ import Runtime


def _ft_scalingfactor(*args, **kwargs):
    """
      FT_SCALINGFACTOR determines the scaling factor from old to new units, i.e. it  
        returns a number with which the data in the old units needs to be multiplied  
        to get it expressed in the new units.   
         
        Use as  
          factor = ft_scalingfactor(old, new)  
        where old and new are strings that specify the units.  
         
        For example  
          ft_scalingfactor('m', 'cm')          % returns 100  
          ft_scalingfactor('V', 'uV')          % returns 1000  
          ft_scalingfactor('T/cm', 'fT/m')     % returns 10^15 divided by 10^-2, which is 10^17  
          ft_scalingfactor('cm^2', 'mm^2')     % returns 100  
          ft_scalingfactor('1/ms', 'Hz')       % returns 1000  
         
        The following fundamental units are supported  
          metre       m   length  l (a lowercase L), x, r L  
          kilogram    kg  mass    m   M  
          second      s   time    t   T  
          ampere      A   electric current    I (an uppercase i)  I  
          kelvin      K   thermodynamic temperature   T   #  
          mole        mol amount of substance n   N  
          candela     cd  luminous intensity  Iv (an uppercase i with lowercase non-italicized v subscript)   J  
         
        The following derived units are supported  
          hertz       Hz  frequency   1/s T-1  
          radian      rad angle   m/m dimensionless  
          steradian   sr  solid angle m2/m2   dimensionless  
          newton      N   force, weight   kg#m/s2 M#L#T-2  
          pascal      Pa  pressure, stress    N/m2    M#L-1#T-2  
          joule       J   energy, work, heat  N#m = C#V = W#s M#L2#T-2  
          coulomb     C   electric charge or quantity of electricity  s#A T#I  
          volt        V   voltage, electrical potential difference, electromotive force   W/A = J/C   M#L2#T-3#I-1  
          farad       F   electric capacitance    C/V M-1#L-2#T4#I2  
          siemens     S   electrical conductance  1/# = A/V   M-1#L-2#T3#I2  
          weber       Wb  magnetic flux   J/A M#L2#T-2#I-1  
          tesla       T   magnetic field strength V#s/m2 = Wb/m2 = N/(A#m)    M#T-2#I-1  
          henry       H   inductance  V#s/A = Wb/A    M#L2#T-2#I-2  
          lumen       lm  luminous flux   cd#sr   J  
          lux         lx  illuminance lm/m2   L-2#J  
          becquerel   Bq  radioactivity (decays per unit time)    1/s T-1  
          gray        Gy  absorbed dose (of ionizing radiation)   J/kg    L2#T-2  
          sievert     Sv  equivalent dose (of ionizing radiation) J/kg    L2#T-2  
          katal       kat catalytic activity  mol/s   T-1#N  
         
        The following alternative units are supported  
          inch        inch  length  
          feet        feet  length  
          gauss       gauss magnetic field strength  
         
        The following derived units are not supported due to potential confusion  
        between their ascii character representation  
          ohm             #   electric resistance, impedance, reactance   V/A M#L2#T-3#I-2  
          watt            W   power, radiant flux J/s = V#A   M#L2#T-3  
          degree Celsius	?C	temperature relative to 273.15 K	K	?  
         
        See also http://en.wikipedia.org/wiki/International_System_of_Units  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/inverse/private/ft_scalingfactor.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_scalingfactor", *args, **kwargs)
