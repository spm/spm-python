from mpython import MatlabClass
from spm._runtime import Runtime, RuntimeMixin


class cfg_inv_out(RuntimeMixin, MatlabClass):
    def __init__(self, *args, **kwargs):
        """
          function obj = cfg_inv_out(varargin)  
            Auxiliary class to mark invalid (i.e. not yet available) outputs of  
            cfg_exbranch'es. An object of this type will be assigned automatically  
            to a cfg_exbranch'es .jout field. resolve_deps will not resolve outputs  
            that consist of a cfg_inv_out object.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
            
              Documentation for cfg_inv_out  
                 doc cfg_inv_out  
            
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_inv_out/cfg_inv_out.m )

        Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """

        super().__init__()
