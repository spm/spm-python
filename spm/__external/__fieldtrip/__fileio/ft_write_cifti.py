from spm.__wrapper__ import Runtime


def ft_write_cifti(*args, **kwargs):
    """
      FT_WRITE_CIFTI writes functional data or functional connectivity to a cifti-2  
        file. The geometrical description of the brainordinates can consist of  
        triangulated surfaces or voxels in a regular 3-D volumetric grid. The functional  
        data can consist of a dense or a parcellated representation. Furthermore, it  
        writes the geometrical description of the surfaces to one or multiple gifti  
        files.  
         
        Use as  
          ft_write_cifti(filename, data, ...)  
        where the filename is a string and the data according to the description below.  
         
        If the input data describes a dense representation of functional data, the data  
        structure should conform to the FT_DATATYPE_SOURCE or FT_DATATYPE_VOLUME  
        definition.  
         
        If the input data describes a parcellated representation of functional data, the  
        data structure should conform to the FT_DATATYPE_TIMELOCK or FT_DATATYPE_FREQ  
        definition. In addition, the description of the geometry should be specified in  
        the data.brainordinate field, which should conform to the FT_DATATYPE_SOURCE or  
        FT_DATATYPE_VOLUME definition.  
         
        Any optional input arguments should come in key-value pairs and may include  
          'parameter'        = string, fieldname that contains the functional data  
          'brainstructure'   = string, fieldname that describes the brain structures (default = 'brainstructure')  
          'parcellation'     = string, fieldname that describes the parcellation (default = 'parcellation')  
          'precision'        = string, can be 'single', 'double', 'int32', etc. (default ='single')  
          'writesurface'     = boolean, can be false or true (default = true)  
          'debug'            = boolean, write a debug.xml file (default = false)  
         
        The brainstructure refers to the global anatomical structure, such as CortexLeft, Thalamus, etc.  
        The parcellation refers to the the detailled parcellation, such as BA1, BA2, BA3, etc.  
         
        See also FT_READ_CIFTI, FT_READ_MRI, FT_WRITE_MRI  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_write_cifti.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_write_cifti", *args, **kwargs, nargout=0)
