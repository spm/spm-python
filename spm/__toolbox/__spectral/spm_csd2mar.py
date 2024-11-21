from spm.__wrapper__ import Runtime


def spm_csd2mar(*args, **kwargs):
    """
      Converts cross spectral density to MAR representation  
        FORMAT [mar] = spm_csd2mar(csd,Hz,p,dt)  
         
        csd  (N,:,:)   - cross spectral density  
        Hz   (n x 1)   - vector of frequencies (Hz)  
        p    (1)       - MAR(p) process    [default: p  = 8]  
        dt             - sampling interval [default: dt = 1/(2*Hz(end))]  
         
        mar  {1}       - see spm_mar  
         
        See also:   
         spm_ccf2csd.m, spm_ccf2mar, spm_csd2ccf.m, spm_csd2mar.m, spm_mar2csd.m,  
         spm_csd2coh.m and spm_Q  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/spectral/spm_csd2mar.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_csd2mar", *args, **kwargs)
