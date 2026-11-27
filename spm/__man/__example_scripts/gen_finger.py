from spm._runtime import Runtime


def gen_finger(*args, **kwargs):
    r"""
      Generate finger movement data  
        FORMAT [yy,P,M,U] = gen_finger(sim)  
         
        sim       Simulation data structure:  
         
                  .Nt         number of trials  
                  .m          first or 2nd order PIF  
                  .init       'partial': initial phase diff  
                              restricted to small range  
                              'full': initial phase diff  
                              uniform in 0 to 2 pi  
                  .noise_dev  STD of additive noise  
                  .do_plot    plot data (1)  
         
        yy        yy{n} for nth trial data  
        P         model parameters  
        M         model structure  
        U         input structure  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/man/example_scripts/gen_finger.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("gen_finger", *args, **kwargs)
