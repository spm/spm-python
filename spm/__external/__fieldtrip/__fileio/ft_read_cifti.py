from spm.__wrapper__ import Runtime


def ft_read_cifti(*args, **kwargs):
    """
      FT_READ_CIFTI read functional data or functional connectivity from a cifti-1 or  
        cifti-2 file. The functional data can consist of a dense or a parcellated  
        representation. The geometrical description of the brainordinates can consist of  
        triangulated surfaces or voxels in a regular 3-D volumetric grid. If available,  
        it also reads the geometrical description of the surfaces from the accompanying  
        gifti files.  
         
        Use as  
          data = ft_read_cifti(filename, ...)  
         
        If the file contains a dense representation of functional data, the output data  
        structure is organized according to the FT_DATATYPE_SOURCE or FT_DATATYPE_VOLUME  
        definition.  
         
        If the contains a parcellated representation of functional data, the output data  
        structure is organized according to the FT_DATATYPE_TIMELOCK or FT_DATATYPE_FREQ  
        definition. In addition, the description of the geometry wil be represented in a  
        data.brainordinate field, which is organized according to the FT_DATATYPE_SOURCE  
        or FT_DATATYPE_VOLUME definition.  
         
        Any optional input arguments should come in key-value pairs and may include  
          'readdata'         = boolean, can be false or true (default depends on file size)  
          'readsurface'      = boolean, can be false or true (default = true)  
          'cortexleft'       = string, filename with left cortex (optional, default is automatic)  
          'cortexright'      = string, filename with right cortex (optional, default is automatic)  
          'hemisphereoffset' = number, amount in milimeter to move the hemispheres apart from each other (default = 0)  
          'mapname'          = string, 'field' to represent multiple maps separately, or 'array' to represent as array (default = 'field')  
          'debug'            = boolean, write a debug.xml file (default = false)  
         
        See also FT_WRITE_CIFTI, FT_READ_MRI, FT_WRITE_MRI  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_read_cifti.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_read_cifti", *args, **kwargs)
