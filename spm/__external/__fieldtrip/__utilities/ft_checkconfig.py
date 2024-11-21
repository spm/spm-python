from spm.__wrapper__ import Runtime


def ft_checkconfig(*args, **kwargs):
    """
      FT_CHECKCONFIG checks the input cfg of the main FieldTrip functions  
         
        It checks whether the cfg contains all the required options, it gives  
        a warning when renamed or deprecated options are used, and it makes sure  
        no forbidden options are used. If necessary and possible, this function  
        will adjust the cfg to the input requirements. If the input cfg does NOT  
        correspond to the requirements, this function gives an elaborate warning  
        message.  
         
        It controls the relevant cfg options that are being passed on to other  
        functions, by putting them into substructures or converting them into the  
        required format.  
         
        Use as  
          [cfg] = ft_checkconfig(cfg, ...)  
         
        The behavior of checkconfig can be controlled by the following cfg options, which  
        can be set as global FieldTrip defaults (see FT_DEFAULTS)  
          cfg.checkconfig = 'pedantic', 'loose' or 'silent', this controls the how strict this function is  
          cfg.checksize   = number in bytes (can be inf), this controls the maximum size of output cfg fields  
         
        Optional input arguments should be specified as key-value pairs and can include  
          renamed         = {'old',  'new'}        % list the old and new option  
          renamedval      = {'opt',  'old', 'new'} % list option and old and new value  
          allowedtype     = {'opt', 'allowed1', ...} % list of allowed data type classes for a particular option, anything else will throw an error  
          allowedval      = {'opt', 'allowed1', ...} % list of allowed values for a particular option, anything else will throw an error  
          required        = {'opt1', 'opt2', etc.} % list the required options  
          allowed         = {'opt1', 'opt2', etc.} % list the allowed options, all other options are forbidden  
          forbidden       = {'opt1', 'opt2', etc.} % list the forbidden options, these result in an error  
          deprecated      = {'opt1', 'opt2', etc.} % list the deprecated options  
          unused          = {'opt1', 'opt2', etc.} % list the unused options, these will be removed and a warning is issued  
          createsubcfg    = {'subname', etc.}      % list the names of the sub-configuration items  
          createtopcfg    = {'subname', etc.}      % list the names of the sub-configuration items  
          dataset2files   = 'yes', 'no'            % converts dataset into headerfile and datafile  
          inside2logical  = 'yes', 'no'            % converts cfg.inside or cfg.sourcemodel.inside into logical representation  
          checksize       = 'yes', 'no'            % remove large fields from the cfg  
         
        See also FT_CHECKDATA, FT_CHECKOPT, FT_DEFAULTS  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_checkconfig.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_checkconfig", *args, **kwargs)
