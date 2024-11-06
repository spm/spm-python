from spm.__wrapper__ import Runtime


def _read_ctf_ascii(*args, **kwargs):
    """
      READ_CTF_ASCII reads general data from an CTF configuration file  
         
        The file should be formatted like  
           Group  
           {  
             item1 : value1a value1b value1c  
             item2 : value2a value2b value2c  
             item3 : value3a value3b value3c  
             item4 : value4a value4b value4c  
           }  
         
        This fileformat structure is used in  
          params.avg  
          default.hdm  
          multiSphere.hdm  
          processing.cfg  
        and maybe for other files as well.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ctf_ascii.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_ctf_ascii", *args, **kwargs)
