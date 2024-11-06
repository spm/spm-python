from spm.__wrapper__ import Runtime


def _read_elec(*args, **kwargs):
    """
      READ_ELEC reads "la/mu" electrode parameters from a MBF electrode file  
        which are used to position them on a triangulated surface  
         
        [el, lab] = read_elec(filename)  
         
        where el = [tri, la, mu]  
        and lab contains the electrode labels (if present)  
         
        See also READ_TRI, TRANSFER_ELEC  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_elec.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_elec", *args, **kwargs)
