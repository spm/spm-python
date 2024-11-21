from spm.__wrapper__ import Runtime


def ft_sourcewrite(*args, **kwargs):
    """
      FT_SOURCEWRITE exports source-reconstructed results to gifti or nifti format file.  
        The appropriate output file depends on whether the source locations are described by  
        on a cortically constrained sheet (gifti) or by a regular 3D lattice (nifti).  
         
        Use as  
         ft_sourcewrite(cfg, source)  
        where source is a source structure obtained from FT_SOURCEANALYSIS and  
        cfg is a structure that should contain  
         
          cfg.filename  = string, filename without the extension  
          cfg.filetype  = string, can be 'nifti', 'gifti' or 'cifti' (default is automatic)  
          cfg.parameter = string, functional parameter to be written to file  
          cfg.precision = string, can be 'single', 'double', etc.  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
        If you specify this the input data will be read from a *.mat  
        file on disk. This mat file should contain only a single variable,  
        corresponding with the input data structure.  
         
        See also FT_SOURCEANALYSIS, FT_SOURCEDESCRIPTIVES, FT_VOLUMEWRITE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_sourcewrite.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_sourcewrite", *args, **kwargs, nargout=0)
