from spm.__wrapper__ import Runtime


def _read_besa_avr(*args, **kwargs):
    """
      READ_BESA_AVR reads average EEG data in BESA format  
         
        Use as  
          [avr] = read_besa_avr(filename)  
         
        This will return a structure with the header information in  
          avr.npnt  
          avr.tsb  
          avr.di  
          avr.sb  
          avr.sc  
          avr.Nchan   (optional)  
          avr.label   (optional)  
        and the ERP data is contained in the Nchan X Nsamples matrix  
          avr.data  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_besa_avr.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_besa_avr", *args, **kwargs)
