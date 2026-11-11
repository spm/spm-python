from spm._runtime import Runtime


def spm_dcm_x_neural(*args, **kwargs):
    r"""
      Return the state and equation of neural mass models  
        FORMAT [x,f,h] = spm_dcm_x_neural(P,'model')  
         
         P      - parameter structure  
        'model' - 'ERP','SEP','CMC','LFP','CMM','NMM', 'MFM' or 'CMM NMDA'  
         
        x   - initial states  
        f   - state equation dxdt = f(x,u,P,M)  - synaptic activity  
        h   - state equation dPdt = f(x,u,P,M)  - synaptic plasticity  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/dcm_meeg/spm_dcm_x_neural.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dcm_x_neural", *args, **kwargs)
