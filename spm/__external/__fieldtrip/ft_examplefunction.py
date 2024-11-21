from spm.__wrapper__ import Runtime


def ft_examplefunction(*args, **kwargs):
    """
      FT_EXAMPLEFUNCTION demonstrates to new developers how a FieldTrip function should look like  
         
        Use as  
          outdata = ft_examplefunction(cfg, indata)  
        where indata is <<describe the type of data or where it comes from>>  
        and cfg is a configuration structure that should contain  
         
        <<note that the cfg list should be indented with two spaces  
         
          cfg.option1    = value, explain the value here (default = something)  
          cfg.option2    = value, describe the value here and if needed  
                           continue here to allow automatic parsing of the help  
         
        The configuration can optionally contain  
          cfg.option3   = value, explain it here (default is automatic)  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also <<give a list of function names, all in capitals>>  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_examplefunction.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_examplefunction", *args, **kwargs)
