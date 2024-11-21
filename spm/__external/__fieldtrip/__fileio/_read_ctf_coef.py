from spm.__wrapper__ import Runtime


def _read_ctf_coef(*args, **kwargs):
    """
      READ_CTF_COEF returns the spatial filter coefficients for the CTF MEG system  
        that has been installed at the F.C. Donders Centre (id 1706)  
         
        This function actually does not read the coefficients from a file, but the   
        coefficients themselves are included in this function.  
         
        The original location of the coefficients included in this file is  
        odin:/opt/ctf/hardware/M016/M017_1706.coef  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ctf_coef.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_ctf_coef", *args, **kwargs)
