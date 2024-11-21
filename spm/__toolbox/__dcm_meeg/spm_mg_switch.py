from spm.__wrapper__ import Runtime


def spm_mg_switch(*args, **kwargs):
    """
      Switching output  
        FORMAT s = spm_mg_switch(V)  
         
        Switching output s: determined by voltage (V) dependent magnesium  
        blockade parameters as per Durstewitz, Seamans & Sejnowski 2000.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_mg_switch.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mg_switch", *args, **kwargs)
