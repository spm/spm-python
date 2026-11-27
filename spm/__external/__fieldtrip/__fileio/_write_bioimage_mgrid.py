from spm._runtime import Runtime


def _write_bioimage_mgrid(*args, **kwargs):
    r"""
      --------------------------------------------------------  
        WRITE_BIOIMAGE_MGRID writes BioImage Suite .mgrid files from a FieldTrip  
        elec datatype structure  
         
        Use as:  
          write_bioimage_mgrid(filename, elec)  
          where filename has an .mgrid file extension and elec has both a label  
          and an elecpos field  
         
        To view the mgrid file in BioImage Suite, ensure that the orientation of  
        the scan (e.g., RAS) corresponds with the orientation of the electrode  
        positions (in head coordinates) of elec  
         
        Copyright (C) 2017, Arjen Stolk & Sandon Griffin  
        --------------------------------------------------------  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/write_bioimage_mgrid.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("write_bioimage_mgrid", *args, **kwargs, nargout=0)
