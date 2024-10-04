from spm.__wrap__ import _Runtime


def gen_finger(*args, **kwargs):
  """  Generate finger movement data  
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
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/man/example_scripts/gen_finger.m)
  """

  return _Runtime.call("gen_finger", *args, **kwargs)
