from spm._runtime import Runtime


def ft_electrodeselection(*args, **kwargs):
    r"""
      FT_ELECTRODESELECTION makes a selection of a predefined set of electrodes.  
         
        Use as  
          selected = ft_electrodeselection(cfg, elec)  
        where the input elec is a set of electrodes, for example from FT_READ_SENS or  
        FT_ELECTRODEPLACEMENT, and cfg is a configuration structure that can contain the  
        following options:  
         
        If you want to make a selection on the basis of a specified list  
          cfg.channel   = Nx1 cell-array with selection of channels (default = 'all'), see FT_CHANNELSELECTION for details  
         
        If you want to make a graphical selection  
          cfg.headshape = a filename containing headshape, a structure containing a  
                          single triangulated boundary, or a Nx3 matrix with surface  
                          points  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also FT_ELECTRODEPLACEMENT, FT_ELECTRODEREALIGN, FT_READ_SENS  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/ft_electrodeselection.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_electrodeselection", *args, **kwargs)
