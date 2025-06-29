from mpython import MatlabClass
from spm._runtime import Runtime, RuntimeMixin


class cfg_leaf(RuntimeMixin, MatlabClass):
    def __init__(self, *args, **kwargs):
        """
          This is currently only a "marker" class that should be inherited by all  
            leaf classes. It does not add fields and does not have methods.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
            
              Documentation for cfg_leaf  
                 doc cfg_leaf  
            
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_leaf/cfg_leaf.m )

        Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """

        super().__init__()

    def disp(self, *args, **kwargs):
        """
          function disp(varargin)  
            This class should not display any information about its structure.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_leaf/disp.m )

        Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("disp", self._as_matlab_object(), *args, **kwargs, nargout=0)

    def display(self, *args, **kwargs):
        """
          function display(varargin)  
            This class should not display any information about its structure.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_leaf/display.m )

        Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("display", self._as_matlab_object(), *args, **kwargs, nargout=0)
