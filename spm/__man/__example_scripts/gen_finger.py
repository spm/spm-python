from spm.__wrapper__ import Runtime


def gen_finger(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/man/example_scripts/gen_finger.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("gen_finger", *args, **kwargs)
