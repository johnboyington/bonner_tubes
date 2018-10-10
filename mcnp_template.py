template = '''Bonner Sphere Template
c
c Updated  7/12/17 by John Boyington 
c 
c ****************************************************************************** 
c                               CELL CARDS 
c ******************************************************************************
c
c                          -----Beam Port------
1 0         11 -15 -13      IMP:N=1  $ BP Inner Region
2 1 -2.699  11 -12  13 -14  IMP:N=1  $ BP Tube
3 0         (-11):(16):(14 11 -12):(13 12 -16)     IMP:N=0
4 1 -2.699  15 -16 18 -13       IMP:N=1 $ Al Tube
5 1 -2.699  15 -20 23 -18       IMP:N=1 $ Tube Plug
6 {} -{}  20 -21 -18      IMP:N=1 $ Tube Filter 1
7 1 -2.699  (24 -18 21 -26):(26 -17 24 -18)   IMP:N=1 $ Foil Holder 
8 0         17 -16 -18       IMP:N=1   
9 5 -7.310 26 -17 -24        IMP:N=1 $ Foils
10 0        15 -20 -23       IMP:N=1
11 0        21 -26 -24       IMP:N=1

c ****************************************************************************** 
c                               SURFACE CARDS 
c ****************************************************************************** 
11 PX     0.0     $ BP Inner
12 PX    50.0     $ BP Outer
13 CX    0.9525   $ BP Inner Diameter
14 CX    1.27     $ BP Outer Diameter
15 PX    14.75     $ Tube Inner
16 PX    55.0     $ Tube Outer
17 PX    {}    $ Foil Holder Outer
18 CX    0.68     $ Tube Diameter
19 PX    49.0     $ Disk Outer
20 PX    15.0    $ Plug Outer
21 PX    {}    $ Filter Outer 1
23 CX    0.50     $ Plug Outer Diameter
24 CX    0.40     $ Foil Holder Diameter
25 CX    0.20     $ Foil Holder Front Diameter
26 PX    {}    $ Foil Holder Middle Inside

c ****************************************************************************** 
c                               DATA CARDS 
c ******************************************************************************
SDEF   POS=1 0 0 AXS=1 0 0 EXT=0 VEC=1 0 0 ERG=D1 RAD=D2 PAR=1 
SI1 {:8.6e} {:8.6e}
SP1 0 1
SI2 0 0.9525
SP2 -21 1
c
NPS 1E7
c
c  -----------------------------------------------------------------------------
c                                                          MATERIAL CARDS
c  -----------------------------------------------------------------------------
c  -----------------------------------------------------------------------------
c  MATERIAL 1:      Al    
c  ---------------------------(density 2.699 g/cm^3)----------------------------
c  -----------------------------------------------------------------------------
M1  13027.70c   -1
c
c  -----------------------------------------------------------------------------
c  MATERIAL 2:      HDPE    
c  ---------------------------(density 0.950 g/cm^3)----------------------------
c  -----------------------------------------------------------------------------
M2     1001     -0.143
       6000     -0.857
MT2    poly.10t
c  -----------------------------------------------------------------------------
c  MATERIAL 3:      ABS    
c  ---------------------------(density 1.070 g/cm^3)----------------------------
c  -----------------------------------------------------------------------------
M3     1001     -0.0811
       6000     -0.85260563
       7014     -0.0662911
c  -----------------------------------------------------------------------------
c  MATERIAL 4:      Poly    
c  ---------------------------(density 1.300 g/cm^3)----------------------------
c  -----------------------------------------------------------------------------
M4     1001     -0.05595
       6000     -0.5035887
       8000     -0.4404612
c  -----------------------------------------------------------------------------
c  MATERIAL 5:      In  
c  ---------------------------(density 7.310 g/cm^3)----------------------------
c  -----------------------------------------------------------------------------
M5    49000     -1
c
c  -----------------------------------------------------------------------------
c  -----------------------------------------------------------------------------
c                                                             TALLY CARDS       
c  -----------------------------------------------------------------------------
c
c  -----------------------------------------------------------------------------
c  TALLY 1:         That disk.
c  -----------------------------------------------------------------------------
F4:N 9
FM4 1 5 102
F14:N 9
c
c ****************************************************************************** 
c                             END OF INPUT FILE
c ******************************************************************************
'''
