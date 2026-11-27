from spm._runtime import Runtime


def spm_MDP_structure_teaching(*args, **kwargs):
    r"""
      Generates probabilistic training sequences for structure learning  
        FORMAT [O,o] = spm_MDP_structure_teaching(MDP,[OPTIONS])  
         
        MDP     - generative process or exemplars  
         
        O{{.}}  - probabilistic exemplars or training sequence  
        o{[.]}  - indices of exemplars or training sequence  
         
        OPTIONS.N  [0]   - suppress neuronal responses  
        OPTIONS.P  [0]   - suppress plotting  
        OPTIONS.B  [0]   - replay  
        OPTIONS.G  [0]   - suppress graphics  
         
        This routine generates a sequence of (probabilistic) outcomes from a  
        specified POMDP structure. This sequence is appropriate for structure  
        learning. It comprises a sequence of epochs, where each epoch is  
        generated in a specific order: starting from the first factor, the  
        outcomes associated with each hidden state are generated under the first  
        path. By construction, the first path is stationary. After all hidden  
        states have generated the outcomes, successive paths are generated  
        starting from each hidden state. After all paths have been generated, the  
        process is repeated for subsequent factors; under the first state and  
        path of previous factors (noting, that the first path is always  
        stationary; i.e., an identity transition mapping). Unless otherwise  
        specified, outcomes comprise two observations.  
         
        This routine is used in conjunction with spm_MDP_structure_learning.m  
        that will, in principle, recover the factorial structure of MDP given,  
        this sequence of observations.  
         
        See: spm_MDP_structure_learning  
       __________________________________________________________________________  
        Copyright (C) 2005 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_MDP_structure_teaching.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_MDP_structure_teaching", *args, **kwargs)
