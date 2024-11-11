from spm.__wrapper__ import Runtime


def _lineattributes_common(*args, **kwargs):
    """
      LINEATTRIBUTES_COMMON implements consistent line attributes for multiple channels/conditions  
          
        This function is used by   
          ft_databrowser  
          ft_multiplotER  
          ft_singleplotER  
          
        It is not yet used by  
          ft_connectivityplot  
          ft_prepare_layout  
          
        Use as  
          [linecolor, linestyle, linewidth] = lineattributes_common(cfg, varargin)  
          
        The input varargin are the data object(s) which are the input of the caller function.  
        The output consists of:  
          
          linecolor = N x 3 x M matrix with RGB values for N channels and M data arguments  
          linestyle = N x M     cell-array with linestyle for N channels and M data arguments  
          linewidth = N x M     matrix with linewidth for N channels and M data arguments    
          
        The configuration can have the following parameters:  
          cfg.colorgroups = char or numeric vector determining whether the  
                              different values are going to be distributed across channels  
                              ('sequential'), or across data arguments ('condition'). Other  
                              possibilities are 'allblacks', 'chantype', 'labelcharI', where  
                              I is a scalar number indicating the I'th character of the label  
                              based on which the grouping is done  
          cfg.stylegroups = char or numeric vector, same possibilities as above, save for 'allblacks'  
          cfg.widthgroups = char or numeric vector, same possibilities as above, save for 'allblacks'  
          cfg.linecolor   = char, Nx3 matrix, or Nx3xM matrix  
          cfg.linestyle   = char, or cell-array  
          cfg.linewidth   = scalar, or NxM matrix  
         
        If cfg.linecolor is a char, it should either be a sequence of characters that can be translated into  
        an RGB value (i.e., any of 'rbgcmykw'), or it can be 'spatial', in which case a color will be assigned  
        based on the layout.color field. Typically, this will be a color that is based on the x/y/z position of   
        the corresponding sensor.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/lineattributes_common.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("lineattributes_common", *args, **kwargs)
