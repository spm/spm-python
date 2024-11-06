from spm.__wrapper__ import Runtime


def _dftfilter(*args, **kwargs):
    """
      DFTFILTER line noise reduction filter for EEG/MEG data  
          
        [filt] = dftfilter(dat, Fsample, Fline)  
         
        where  
          dat        data matrix (Nchans X Ntime)  
          Fsample    sampling frequency in Hz  
          Fline      line noise frequency  
         
        The line frequency should be specified as a single number.   
        If omitted, a European default of 50Hz will be assumed.  
         
        Preferaby the data should have a length that is a multiple   
        of the period of oscillation of the line noise (20ms for  
        50Hz noise).  
         
        See also NOTCHFILTER,  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/dftfilter.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("dftfilter", *args, **kwargs)
