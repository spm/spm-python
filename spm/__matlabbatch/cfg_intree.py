from spm.__wrapper__ import Runtime, MatlabClassWrapper


class cfg_intree(MatlabClassWrapper):
    def __init__(self, *args, _objdict=None, **kwargs):
        """
          This is currently only a "marker" class that should be inherited by all  
            within-tree classes. It does not add fields and does not have methods.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
            
              Documentation for cfg_intree  
                 doc cfg_intree  
            
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_intree/cfg_intree.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        if _objdict is None:
            _objdict = Runtime.call("cfg_intree", *args, **kwargs)
            
        super().__init__(_objdict)
