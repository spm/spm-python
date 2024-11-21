from spm.__wrapper__ import Runtime


def _write_bioimage_mgrid(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/write_bioimage_mgrid.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("write_bioimage_mgrid", *args, **kwargs, nargout=0)
