from spm._runtime import Runtime


def _read_ctf_sens(*args, **kwargs):
    r"""
      READ_CTF_SENS reads MEG sensor information from CTF configuration file  
         
        magn = read_ctf_sens(filename)  
         
        where the returned structure meg has the fields  
          magn.pnt    position first coil  
          magn.ori    orientation first coil  
          magn.pnt2   position second coil  
          magn.ori2   orientation second coil  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_ctf_sens.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_ctf_sens", *args, **kwargs)
