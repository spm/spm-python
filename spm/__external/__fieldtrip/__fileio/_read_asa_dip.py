from spm._runtime import Runtime


def _read_asa_dip(*args, **kwargs):
    r"""
      READ_ASA_DIP reads the dipole position, moment and amplitude  
        This importer is designed for fixed-dipole models and only supports   
        a limited number of the options that ASA has.  
         
        Use as  
          [pos, mom, ampl, time] = read_asa_dip(filename)  
         
        See also READ_ASA_VOL, READ_ASA_MRI  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/read_asa_dip.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_asa_dip", *args, **kwargs)
