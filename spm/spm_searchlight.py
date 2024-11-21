from spm.__wrapper__ import Runtime


def spm_searchlight(*args, **kwargs):
    """
      Local mass-multivariate (c.f., searchlight) facility  
        FORMAT R = spm_searchlight(SPM,searchopt,fun,varargin)  
        SPM       - structure with fields:  
           .xY.VY - filenames char array or spm_vol struct array of images  
           .VM    - filename or spm_vol structure to a mask (binary) image  
                    Mask image can have any orientation, voxel size or data type.  
                    It is interpolated using nearest neighbour interpolation to  
                    the voxel locations of the data.  
                    If empty, all voxels are used.  
        searchopt - searchlight options using VOI structure (xY) from spm_ROI  
           .def   - searchlight definition {['sphere'] 'box'}  
           .spec  - searchlight parameters [sphere radius {mm}]  
        fun       - function handle to a function that takes three input arguments:  
                      a [n x v] matrix (nb images x nb voxels within searchlight)  
                      a [3 x v] matrix of voxels location within searchlight {vox}  
                      a list of parameters provided in varargin  
                    and returns a vector value [1 x N]  
        varargin  - list of parameters sent to fun  
         
        R         - a [N x 1] cell array with each output (fun nargout) reshaped  
                    to a volume or directly a volume if N == 1  
                    Values outside the mask are attributed NaN.  
       __________________________________________________________________________  
         
        References:  
         
        [1] Adaptive Analysis of fMRI Data. Friman O, Borga M, Lundberg P and   
        Knutsson H. (2003) NeuroImage 19(3):837-845.  
         
        [2] Information-based functional brain mapping. Kriegeskorte N, Goebel R,  
        Bandettini P. (2006) PNAS 103: 3863-3868.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_searchlight.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_searchlight", *args, **kwargs)
