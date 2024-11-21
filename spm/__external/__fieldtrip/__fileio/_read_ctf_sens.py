from spm.__wrapper__ import Runtime


def _read_ctf_sens(*args, **kwargs):
    """
      READ_CTF_SENS reads MEG sensor information from CTF configuration file  
         
        magn = read_ctf_sens(filename)  
         
        where the returned structure meg has the fields  
          magn.pnt    position first coil  
          magn.ori    orientation first coil  
          magn.pnt2   position second coil  
          magn.ori2   orientation second coil  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ctf_sens.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_ctf_sens", *args, **kwargs)
