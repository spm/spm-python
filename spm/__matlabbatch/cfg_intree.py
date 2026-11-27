from mpython import MatlabClass
from spm._runtime import Runtime, RuntimeMixin


class cfg_intree(RuntimeMixin, MatlabClass):
    def __init__(self, *args, **kwargs):
        r"""
          This is currently only a "marker" class that should be inherited by all  
            within-tree classes. It does not add fields and does not have methods.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
            
              Documentation for cfg_intree  
                 doc cfg_intree  
            
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/matlabbatch/@cfg_intree/cfg_intree.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        super().__init__()

    def disp(self, *args, **kwargs):
        r"""
          function disp(varargin)  
            This class should not display any information about its structure.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/matlabbatch/@cfg_intree/disp.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("disp", self._as_matlab_object(), *args, **kwargs, nargout=0)

    def display(self, *args, **kwargs):
        r"""
          function display(varargin)  
            This class should not display any information about its structure.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        Generated from SPM26.10.01.

        [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/matlabbatch/@cfg_intree/display.m )

        Copyright (C) 1995-2026 Functional Imaging Laboratory, 
        Department of Imaging Neuroscience, UCL
        """

        return Runtime.call("display", self._as_matlab_object(), *args, **kwargs, nargout=0)
